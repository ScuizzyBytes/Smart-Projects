import math
import random
import pygame

WIDTH, HEIGHT = 600, 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Game")
clock = pygame.time.Clock()

stars = []
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # --- 1. СПАВН ЗВЕЗД ---
  # Каждый кадр добавляем новые звезды, если их меньше 150
  if len(stars) < 150:
    angle = random.uniform(0, 2 * math.pi)  # Случайный угол во все стороны
    speed = random.uniform(1.0, 3.0)  # Скорость полета
    stars.append({
        "x": CENTER_X,
        "y": CENTER_Y,
        "vx": math.cos(angle) * speed,  # Вектор скорости по X
        "vy": math.sin(angle) * speed,  # Вектор скорости по Y
    })

  # --- 2. ОБНОВЛЕНИЕ ПОЗИЦИЙ ---
  for star in stars:
    star["x"] += star["vx"]
    star["y"] += star["vy"]

  # Удаляем звезды, которые улетели за границы экрана (чтобы не жрали память)
  stars = [s for s in stars if 0 <= s["x"] <= WIDTH and 0 <= s["y"] <= HEIGHT]

  # --- 3. ОТРИСОВКА ---
  screen.fill((155, 50, 105))  # Розовый фон

  # Сначала рисуем вылетающие звезды (черные точки)
  for star in stars:
    pygame.draw.circle(
        screen, (0, 0, 0), (int(star["x"]), int(star["y"])) , 2
    )

  # Поверх звезд рисуем саму черную дыру в центре
  pygame.draw.circle(screen, (0, 0, 0), (CENTER_X, CENTER_Y), 50)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()