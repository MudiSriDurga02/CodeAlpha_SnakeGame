import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize variables
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_x_change, snake_y_change = 0, 0
snake_length = 1
snake_body = [(snake_x, snake_y)]

food_x, food_y = (
    random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE),
    random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE),
)

score = 0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = SNAKE_SIZE
                snake_x_change = 0

    # Update snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collisions
    if (
        snake_x < 0
        or snake_x >= WIDTH
        or snake_y < 0
        or snake_y >= HEIGHT
        or (snake_x, snake_y) in snake_body[1:]
    ):
        game_over = True

    # Add snake's head to the body
    snake_body.insert(0, (snake_x, snake_y))

    # Check if snake ate the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x, food_y = (
            random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE),
            random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE),
        )
    else:
        snake_body.pop()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update the display
    pygame.display.update()

    # Control game speed
    time.sleep(1 / SNAKE_SPEED)

# Game over message
font = pygame.font.Font(None, 36)
game_over_text = font.render(f"Game Over - Score: {score}", True, RED)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WIDTH // 2, HEIGHT // 2)
screen.blit(game_over_text, game_over_text_rect)

pygame.display.update()

# Wait for a key press to exit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()