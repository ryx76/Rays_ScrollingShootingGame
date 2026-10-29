# Development Process

## Initial Idea

I wanted to create a small scrolling shooter with simple controls and clear feedback. Players move an aircraft, shoot enemies, and try to survive while earning points.

I first used code generated with ChatGPT to build the game locally in Processing. I created all the image assets myself, including the aircraft, enemies, bullets, background, and interface graphics.

## User Testing and Improvement

I asked another person to try the Processing version. Initially, the game had no start or game-over screen, so the experience lacked a clear beginning, ending, and way to play again.

After testing, I added both screens to complete the interaction loop:

**Start → Play → Game over → Restart**

This made the next action clearer without adding unnecessary gameplay features.

## Python Port

For this assignment, I asked ChatGPT to recreate the Processing game in Python with Pygame, keeping my original artwork and main mechanics.

The port preserved movement, shooting, two enemy types, scoring, three lives, bullet cancellation, and the penalty for enemies escaping. It also added manual pause, automatic pause when switching windows, and cleanup of off-screen bullets.

Automatic pause handles a common interruption: players can return to the window and press **P** to continue without losing lives while away.

## Setup and Web Publishing

Local installation initially failed because of a Python/Pygame compatibility issue. Running the game with Python 3.12 resolved it.

Publishing required enabling GitHub Pages and correcting the dependency declaration for the browser runtime. An older cached package also caused a black screen in the normal browser, while the updated game ran successfully in a private window. A versioned package filename was proposed to prevent old packages from being reused after updates.

This process showed me that a successful deployment still needs to be checked by opening and playing the published game.

## AI Usage and Reflection

ChatGPT generated the initial Processing code, most of the Python port, and the deployment configuration. It also helped explain commands, troubleshoot errors, and draft documentation.

I created the artwork, chose the game direction, ran the project, arranged user testing, and decided to add the start and game-over screens.

I adopted the suggestion to add automatic pause. An AI-generated dependency setting needed revision after it caused a browser startup error.

The main improvement was turning the shooting prototype into a complete, repeatable experience. The user test described above was conducted on the Processing version; further testing of the final browser version would help check loading and keyboard input on other computers.