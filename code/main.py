import pygame
from os.path import join

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT  = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# import an image
player_surf = pygame.image.load(join('images', 'player.png'))

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the game
    display_surface.fill('darkgray')
    x += 0.1
    # the ship is positioned at (x, 250)
    display_surface.blit(player_surf, (x,250))
    pygame.display.update() #update updates the entire window
    

# Closing the game properly to avoid weird behaviour   
pygame.quit()

# Stannar 36:05 https://www.youtube.com/watch?v=8OMghdHP-zs