# Rays_ScrollingShootingGame
# Ray's Scrolling Shooting Game

## [▶ PLAY THE GAME ONLINE](https://ryx76.github.io/Rays_ScrollingShootingGame/)

**Open the link on a computer with a keyboard. No installation is required.**

Wait for **Ready to start**, click to launch, then press **Space** to begin. If the controls do not respond, click inside the game and switch to English input mode.

---

## About the Game

This is a 2D vertical scrolling shooter, originally developed in Processing and later recreated in Python with Pygame.

The player controls an aircraft, shoots incoming enemies, and tries to survive while earning a higher score. It is designed for players who enjoy short arcade games with simple keyboard controls.

Moving and shooting produce immediate visual feedback through aircraft movement, bullets, enemy destruction, changes in lives, and score updates. Start and game-over screens connect individual rounds into a complete, repeatable experience.

## Controls

| Key | Action |
| --- | --- |
| Space | Start / restart after game over |
| W / A / S / D | Move up / left / down / right |
| Hold J | Shoot continuously |
| P | Pause / resume |

Switching away from the game window automatically pauses the game. Return to the game and press **P** to continue.

## Game Rules

- The player starts with **3 lives**.
- Ordinary enemies fire downward, take **1 hit** to destroy, and award **1 point**.
- Accelerating enemies do not shoot, take **2 hits** to destroy, and award **2 points**.
- Enemies appear in a repeating sequence of three ordinary enemies followed by one accelerating enemy.
- Colliding with an enemy, being hit by an enemy bullet, or allowing an enemy to escape through the bottom costs **1 life**.
- Player bullets and enemy bullets cancel each other when they collide.
- Enemy spawning becomes more demanding over time.
- When lives reach zero, the game-over screen appears with the final score. Press **Space** to start another round.

## Run Locally

Install [uv](https://docs.astral.sh/uv/), then run these commands in a terminal:

```powershell
git clone https://github.com/ryx76/Rays_ScrollingShootingGame.git
cd Rays_ScrollingShootingGame
uv run --python 3.12 main.py
```

If the project is already downloaded, open its folder in VS Code and run:

```powershell
uv run --python 3.12 main.py
```

Keep the `data` folder beside `main.py`, as it contains the images required by the game.

Close the game window to quit.

See [PROCESS.md](PROCESS.md) for the development process, user testing, design changes, and AI usage.