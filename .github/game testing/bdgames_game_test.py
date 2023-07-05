import pygame
import sys

# Initialize Pygame
pygame.init()

# Set window dimensions
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Click Game")

# Load images
background_img = pygame.image.load("background.jpg")
sprite1_img = pygame.image.load("sprite1.png")
sprite2_img = pygame.image.load("sprite2.png")
error_img = pygame.image.load("error.png")

# Set sprite positions
sprite1_x = WIDTH // 4 - sprite1_img.get_width() // 2
sprite1_y = HEIGHT // 2 - sprite1_img.get_height() // 2

sprite2_x = 3 * WIDTH // 4 - sprite2_img.get_width() // 2
sprite2_y = HEIGHT // 2 - sprite2_img.get_height() // 2

# Set text properties
font = pygame.font.Font(None, 36)
text = font.render("Press to Start", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Set blinking properties
blink_interval = 500  # milliseconds
blink_timer = 0
show_text = True

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Show error image when clicked
            window.blit(error_img, (0, 0))
            pygame.display.flip()

    # Blinking logic
    current_time = pygame.time.get_ticks()
    if current_time - blink_timer >= blink_interval:
        show_text = not show_text
        blink_timer = current_time

    # Draw
    window.blit(background_img, (0, 0))
    window.blit(sprite1_img, (sprite1_x, sprite1_y))
    window.blit(sprite2_img, (sprite2_x, sprite2_y))
    
    if show_text:
        window.blit(text, text_rect)

    # Update the window
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
