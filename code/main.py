import pygame
from os.path import join
from random import randint

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

# import an image, the space ship and stars. Use convert/convert_alpha for improved performance
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]

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
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    pygame.display.update() #update updates the entire window
    
    

# Closing the game properly to avoid weird behaviour   
pygame.quit()

# Stannar 42:15 https://www.youtube.com/watch?v=8OMghdHP-zs