import math
import random

import pygame

print("[TIP]: Don't worry, it won't lag even if you put at least 1 million")
question = int(input("How Much Stars You Want?: "))

pygame.init()

W, H = 700, 700
CENTER_X, CENTER_Y = W / 2, H / 2

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Random Color")
clock = pygame.time.Clock()

fade_surface = pygame.Surface((W, H), pygame.WINDOWCLOSE)
fade_surface.fill((0, 0, 0))
fade_surface.set_alpha(40)
running = True

stars = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if len(stars) < question:
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 3)
        random_color1 = random.randint(0, 255)
        random_color2 = random.randint(0, 255)
        random_color3 = random.randint(0, 255)

        stars.append({
            "x": CENTER_X,
            "y": CENTER_Y,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "color": (random_color1, random_color2, random_color3)
        })
    
    for star in stars:
        star["x"] += star["vx"]
        star["y"] += star["vy"]
    
    screen.blit(fade_surface,(0, 0))
    
    for star in stars:
        pygame.draw.circle(screen, star["color"], (int(star["x"]), int(star["y"])) , 5)
    
    pygame.draw.circle(screen, (255, 255, 255), (CENTER_X, CENTER_Y), 50)
    
    pygame.display.flip()
    
    clock.tick(60)

print(star["color"])
pygame.quit()
