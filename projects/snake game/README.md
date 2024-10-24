# Snake Game:

* Welcome to the Snake Game! This is a classic arcade-style game where you control a snake that grows longer as it eats food. Your goal is to avoid hitting the walls or colliding with your own tail while scoring as many points as possible.

## Overview:

* In this game, you control a snake on a grid-like screen using the arrow keys. The snake's goal is to eat food that randomly appears on the screen. Each time the snake eats, it grows longer, and your score increases. However, be careful! If you run into the walls or your own tail, the game will end.

* The project uses the turtle module from Python to handle graphics and game mechanics. The game updates in real time and incorporates simple collision detection.

* I've also added a **highest score tracker** that keeps track of your best score across different game sessions. Your highest score is saved in a file and updated whenever you beat your previous high score.

## How to Play:

1. Use the arrow keys on your keyboard to control the snake's movement:
   - Up Arrow: Move up
   - Down Arrow: Move down
   - Left Arrow: Move left
   - Right Arrow: Move right
2. The snake will automatically move forward, so your job is to change its direction to eat the food and avoid crashing into walls or itself.

3. The game ends if:
   - The snake hits the boundary walls.
   - The snake collides with its own tail.
4. Your score increases by 1 every time the snake eats the food.

## Features:

* **Snake Movement**: The snake can move in four directions (up, down, left, right).
* **Food**: Randomly appearing food increases the length of the snake and your score.
* **Scoreboard**: A simple scoreboard tracks your current score and your highest score across all sessions.
* **Highest Score Tracker**: The game now tracks your highest score, saving it between game sessions.
* **Collision Detection**: Detects collisions with the walls or the snake's own tail, ending the game when necessary.

## Files:

* `main.py`: 
   The main script that sets up the game screen and handles the game loop. It initializes the snake, food, and scoreboard, and listens for user input to control the snake's movement.

* `snake.py`: 
   Contains the Snake class, which defines the behavior of the snake, including movement, growing longer when it eats food, and detecting collisions.

* `food.py`: 
   Contains the Food class, which defines how the food appears on the screen at random locations and is refreshed after being eaten.

* `score.py`: 
   Contains the Score class, which handles the scoreboard, updating the score, tracking the highest score, and displaying a "Game Over" message when the game ends.
