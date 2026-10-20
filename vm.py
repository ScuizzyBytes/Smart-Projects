import math
import random

import pygame

WIDTH, HEIGHT = 600, 600 
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Game")
clock = pygame.time.Clock()

running = True
stars = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if len(stars) < 350:
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1.0, 3.0)
        
        stars.append({
            "x": CENTER_X,
            "y": CENTER_Y,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed
        })
    
    for star in stars:
        star["x"] += star["vx"]
        star["y"] += star["vy"]
            
    screen.fill((155, 50, 105))
    
    for star in stars:
        pygame.draw.circle(screen, (0, 0, 0), (int(star["x"]), int(star["y"])), 2)
    
    pygame.draw.circle(screen, (0, 0, 0), (CENTER_X, CENTER_Y), 50)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()