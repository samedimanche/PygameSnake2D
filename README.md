# PygameSnake2D

**PygameSnake2D** is a simple 2D Snake game implemented using the **Pygame** library in Python. This project demonstrates the basics of game development, including handling user input, rendering graphics, and managing game logic. It is a great starting point for anyone interested in learning how to create games with Python and Pygame.

---

## Overview

The game features a classic Snake gameplay experience:
- The player controls a snake that moves around the screen.
- The snake grows in length when it eats food.
- The game ends if the snake collides with the walls or itself.

This project was developed **for educational purposes** to explore the capabilities of the Pygame library and to provide a foundation for building more complex games.

---

## Features

- **Simple Gameplay**: Easy-to-understand mechanics with intuitive controls.
- **Dynamic Food Spawning**: Food appears at random positions on the screen.
- **Snake Growth**: The snake grows longer as it consumes food.
- **Collision Detection**: The game ends if the snake collides with the walls or its own body.
- **Customizable Settings**: Adjustable snake speed and window size.

---

## Technologies Used

- **Python**: The core programming language used for the game.
- **Pygame**: A popular library for creating 2D games in Python.
- **Random Module**: Used to generate random positions for the food.

---

## How It Works

1. **Initialization**:
   - Pygame is initialized, and the game window is set up with a width of 800 pixels and a height of 600 pixels.
   - Colors for the background, snake, and food are defined.
   - Game variables such as snake size, speed, and initial position are set.

2. **Game Loop**:
   - The game runs in a loop until the player quits or the game is over.
   - The player controls the snake's direction using the arrow keys.
   - The snake moves in the current direction, and its body is updated.
   - Collisions with walls or the snake's own body end the game.
   - If the snake eats the food, its length increases, and new food is spawned at a random location.

3. **Rendering**:
   - The game window is cleared and redrawn in each iteration of the game loop.
   - The snake and food are rendered using rectangles.

4. **Game Over**:
   - The game ends when a collision is detected, and Pygame is shut down.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/PygameSnake2D.git
   cd PygameSnake2D
   ```

2. **Install Dependencies**:
   - Install the `pygame` library if not already installed:
     ```bash
     pip install pygame
     ```

3. **Run the Game**:
   ```bash
   python main.py
   ```

---

## Controls

- **Arrow Keys**: Control the direction of the snake.
  - **Up Arrow**: Move up.
  - **Down Arrow**: Move down.
  - **Left Arrow**: Move left.
  - **Right Arrow**: Move right.

---

## Disclaimer

This project was developed **for educational purposes only**. It is not intended for commercial use, and no part of this project is monetized. The author is not responsible for any misuse of the code or its consequences.

---

## Contribution

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Thank you for your interest in this project! For more details, feel free to explore the repository and reach out with any questions.
