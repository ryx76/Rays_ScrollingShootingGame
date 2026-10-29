# Aircraft Battle — Python port

Original Processing game: Yixuan Rui. Python port produced with ChatGPT assistance.
Original image assets retained from the supplied project; their original external sources, if any, should be credited by the author before publishing.

Run: `uv run main.py`
Controls: Space starts/restarts; WASD moves; hold J to shoot; P pauses/resumes.
Switching windows pauses play. Press P after returning.

Preserved: 3 lives, enemy escape penalty, bullet cancellation, 3 ordinary enemies then 1 accelerating enemy, scores 1/2 and health 1/2, progressive spawning.
Port changes: frame-independent movement based on 60 FPS; spawn timers reset each round; safe collision iteration; off-screen bullets cleaned up; pause/focus handling. Enemy bullets disappear with their owning enemy, as in the original.

Browser build: `uv run --with pygbag==0.9.2 python -m pygbag .`
Open http://localhost:8000 and click the game to focus it.
GitHub Pages workflow is included. Enable Settings > Pages > Source: GitHub Actions, then push to main or manually run the workflow.
Browser runtime downloads require internet. Desktop keyboard controls; no touch controls.

Validation: headless 600-frame simulation, rendering and reset checks passed. Real user testing and live GitHub Pages deployment must still be completed. Do not describe these as already done in PROCESS.md.
Keep your existing README.md and PROCESS.md; this package deliberately does not overwrite them. Add project description, run instructions, screenshot, credits, AI disclosure and actual user trial observations there.
