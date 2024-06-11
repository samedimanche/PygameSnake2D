import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define game variables
snake_size = 10
snake_speed = 15

# Initialize the snake
snake_x = window_width // 2
snake_y = window_height // 2
snake_body = [(snake_x, snake_y)]
snake_length = 1

# Initialize the food
food_x = random.randrange(0, window_width - snake_size, snake_size)
food_y = random.randrange(0, window_height - snake_size, snake_size)

# Initialize the game loop variables
game_over = False
clock = pygame.time.Clock()

# Define movement directions
UP = (0, -snake_size)
DOWN = (0, snake_size)
LEFT = (-snake_size, 0)
RIGHT = (snake_size, 0)
direction = RIGHT

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Move the snake
    snake_x += direction[0]
    snake_y += direction[1]
    snake_body.insert(0, (snake_x, snake_y))

    # Check for collisions
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height or (snake_x, snake_y) in snake_body[1:]:
        game_over = True

    # Check if the snake ate the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randrange(0, window_width - snake_size, snake_size)
        food_y = random.randrange(0, window_height - snake_size, snake_size)
        snake_length += 1
    else:
        snake_body.pop()

    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(window, RED, (food_x, food_y, snake_size, snake_size))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
