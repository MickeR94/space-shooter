import pygame


#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT  = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True


while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the game
    display_surface.fill("blue")
    pygame.display.update() #update updates the entire window
    

# Closing the game properly to avoid weird behaviour   
pygame.quit()

# Stannar 16:04 https://www.youtube.com/watch?v=8OMghdHP-zs