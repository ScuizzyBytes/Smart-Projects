import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 700, 550

x_cordinates = 350
y_cordinates = 275

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

clock = pygame.time.Clock()
running = True

def create_block(x, y):

    pygame.draw.circle(screen, (0, 255, 0), (x, y), 20)

def move_block(event, y_cord, x_cord):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_cord -= 20
        elif event.key == pygame.K_DOWN:
            y_cord += 20
        elif event.key == pygame.K_LEFT:
            x_cord -= 20
        elif event.key == pygame.K_RIGHT:
            x_cord += 20

    return x_cord, y_cord


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        x_cordinates, y_cordinates = move_block(event, y_cordinates, x_cordinates)

    screen.fill((0, 0, 0))

    create_block(x_cordinates, y_cordinates)

    pygame.display.flip()

    clock.tick(60)
    
        
pygame.quit()
sys.exit()