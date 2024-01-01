import pygame
import sys
#  Pygame initialization
pygame.init()
# Window parameters
width, height = 400, 400
bg_color = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dessin de personne")
# Colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(bg_color)

    # Draw the person
    pygame.draw.circle(screen, black, (200, 100), 50)
    pygame.draw.rect(screen, black, (175, 150, 50, 100))
    pygame.draw.line(screen, black, (175, 175), (125, 275), 3)
    pygame.draw.line(screen, black, (225, 175), (275, 275), 3)
    pygame.draw.line(screen, black, (200, 250), (150, 350), 3)
    pygame.draw.line(screen, black, (200, 250), (250, 350), 3)

    # Add the message "Happy New Year 2024"
    font = pygame.font.Font(None, 24)
    text = font.render("Happy New Year 2024", True, black)
    screen.blit(text, (width // 2 - text.get_width() // 2, height - 50))

    # Update the screen
    pygame.display.flip()