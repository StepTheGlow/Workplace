import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Workemon")

# Load the background image
background_image = pygame.image.load("background.png").convert()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    window.blit(background_image, (0, 0))

    # Add additional drawing and user interaction code here

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
