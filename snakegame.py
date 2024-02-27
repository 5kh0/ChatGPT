import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake
snake_size = 20
snake_speed = 15
snake = [(100, 100)]
snake_direction = (1, 0)

# Food
food_size = 20
food = (random.randint(0, (WIDTH - food_size) // food_size) * food_size,
        random.randint(0, (HEIGHT - food_size) // food_size) * food_size)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * snake_size
    y += snake_direction[1] * snake_size
    snake.insert(0, (x, y))

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, (WIDTH - food_size) // food_size) * food_size,
                random.randint(0, (HEIGHT - food_size) // food_size) * food_size)
    else:
        snake.pop()

    # Check for collisions with the walls
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Check for collisions with itself
    if len(snake) > 1 and snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    # Draw the background
    win.fill(WHITE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Draw the food
    pygame.draw.rect(win, RED, (food[0], food[1], food_size, food_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(snake_speed)
