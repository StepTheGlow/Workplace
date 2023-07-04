import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Intro")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the font
font = pygame.font.SysFont(None, 40)

# Set up the clock
clock = pygame.time.Clock()

# Animation variables
text_alpha = 0
text_direction = 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update animation
    text_alpha += text_direction
    if text_alpha > 255:
        text_alpha = 255
        text_direction = -1
    elif text_alpha < 0:
        text_alpha = 0
        text_direction = 1

    # Clear the screen
    screen.fill(BLACK)

    # Render the "Press Start" text
    text = font.render("Press Start", True, (255, 255, 255, text_alpha))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

