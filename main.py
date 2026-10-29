# /// script
# requires-python = ">=3.11"
# dependencies = ["pygame-ce==2.5.3"]
# ///
"""Python port of Yixuan Rui's Processing aircraft game."""
import asyncio
import random
from pathlib import Path
import pygame

W, H = 500, 1000
ROOT = Path(__file__).resolve().parent

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption('Aircraft Battle')
        self.clock = pygame.time.Clock()
        self.images = {}
        for name in ['background.jpg', 'start-page.png', 'gameOver.png', 'life.png',
                     'myPlane.png', 'enemy1.png', 'enemy2.png', 'mybomb.png', 'enemybomb.png']:
            self.images[name] = pygame.image.load(str(ROOT / 'data' / name)).convert_alpha()
        self.font = pygame.font.Font(None, 30)
        self.state = 'start'
        self.bg_y = 0
        self.reset()

    def reset(self):
        self.player = pygame.Vector2(100, 500)
        self.life, self.score = 3, 0
        self.enemies, self.bullets = [], []
        self.elapsed = self.spawn_timer = self.shot_timer = 0
        self.spawn_interval, self.spawn_count = 2.0, 0

    def rect(self, position, image):
        return self.images[image].get_rect(topleft=position)

    def update(self, dt, keys):
        self.elapsed += dt
        self.player.x += (keys[pygame.K_d] - keys[pygame.K_a]) * 300 * dt
        self.player.y += (keys[pygame.K_s] - keys[pygame.K_w]) * 300 * dt
        size = self.images['myPlane.png'].get_size()
        self.player.x = max(0, min(W-size[0], self.player.x))
        self.player.y = max(0, min(H-size[1], self.player.y))
        self.shot_timer = max(0, self.shot_timer-dt)
        if keys[pygame.K_j] and self.shot_timer <= 0:
            self.bullets.append(pygame.Vector2(self.player.x+size[0]/2-10, self.player.y))
            self.shot_timer = 1/3
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            if len(self.enemies) < 4 + int(self.elapsed/10):
                kind = 2 if self.spawn_count % 4 == 3 else 1
                self.spawn_count += 1
                self.enemies.append(dict(pos=pygame.Vector2(random.uniform(0,400),0),
                                         kind=kind, hp=kind, speed=6.0, timer=0.0, bullets=[]))
                if kind == 2:
                    self.spawn_interval = max(.5, self.spawn_interval-1/60)
        for b in self.bullets:
            b.y -= 600*dt
        self.bullets = [b for b in self.bullets if b.y > -self.images['mybomb.png'].get_height()]
        player_rect = self.rect(self.player,'myPlane.png')
        for e in self.enemies[:]:
            if e['kind'] == 2:
                e['speed'] += 360*dt
                e['pos'].y += e['speed']*dt
            else:
                e['pos'].y += 120*dt
                e['timer'] += dt
                if e['timer'] >= 1:
                    e['timer'] -= 1
                    im = self.images['enemy1.png']
                    e['bullets'].append(pygame.Vector2(e['pos'].x+im.get_width()/2-10,e['pos'].y+im.get_height()))
            er = self.rect(e['pos'],f"enemy{e['kind']}.png")
            if e['pos'].y >= H or player_rect.colliderect(er):
                self.life -= 1
                self.enemies.remove(e)
                continue
            for b in e['bullets'][:]:
                b.y += 300*dt
                br = self.rect(b,'enemybomb.png')
                if b.y > H:
                    e['bullets'].remove(b)
                elif br.colliderect(player_rect):
                    self.life -= 1
                    e['bullets'].remove(b)
                else:
                    for own in self.bullets[:]:
                        if br.colliderect(self.rect(own,'mybomb.png')):
                            e['bullets'].remove(b)
                            self.bullets.remove(own)
                            break
            for b in self.bullets[:]:
                if er.colliderect(self.rect(b,'mybomb.png')):
                    self.bullets.remove(b)
                    e['hp'] -= 1
                    if e['hp'] <= 0:
                        self.score += e['kind']
                        self.enemies.remove(e)
                        break
        if self.life <= 0:
            self.life = 0
            self.state = 'over'

    def draw(self):
        bg = self.images['background.jpg']
        for y in range(-bg.get_height(), H+bg.get_height(), bg.get_height()):
            self.screen.blit(bg,(0,y+int(self.bg_y)))
        if self.state == 'start':
            self.screen.blit(self.images['start-page.png'],(0,0))
        elif self.state == 'over':
            self.screen.blit(self.images['gameOver.png'],(0,0))
        else:
            self.screen.blit(self.images['myPlane.png'],self.player)
            for b in self.bullets:
                self.screen.blit(self.images['mybomb.png'],b)
            for e in self.enemies:
                self.screen.blit(self.images[f"enemy{e['kind']}.png"],e['pos'])
                for b in e['bullets']:
                    self.screen.blit(self.images['enemybomb.png'],b)
        if self.state != 'start':
            heart = self.images['life.png']
            for i in range(self.life):
                self.screen.blit(heart,(12+i*(heart.get_width()+10),H-heart.get_height()-12))
            label = self.font.render(f'Score: {self.score}',True,'white')
            self.screen.blit(label,(W-label.get_width()-12,960))
        if self.state == 'paused':
            label = self.font.render('Paused - P to resume',True,'white')
            self.screen.blit(label,label.get_rect(center=(W/2,H/2)))
        pygame.display.flip()

async def main():
    game = Game()
    running = True
    while running:
        dt = min(game.clock.tick(60)/1000,.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.WINDOWFOCUSLOST and game.state == 'play':
                game.state = 'paused'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.state in ('start','over'):
                    game.reset()
                    game.state = 'play'
                elif event.key == pygame.K_p and game.state in ('play','paused'):
                    game.state = 'paused' if game.state == 'play' else 'play'
        if game.state == 'play':
            game.update(dt,pygame.key.get_pressed())
        game.bg_y = (game.bg_y+120*dt)%game.images['background.jpg'].get_height()
        game.draw()
        await asyncio.sleep(0)
    pygame.quit()

if __name__ == '__main__':
    asyncio.run(main())
