import random

from pygame.locals import *

import pygame


class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = options.get("fontname", None)
        self.fontsize = options.get("fontsize", 72)
        self.fontcolor = options.get("fontcolor", Color("black"))
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)  

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self, surface):
        surface.blit(self.img, self.rect)


class PygameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Math Pygame")
        
        self.t = Text("Pygame App", pos=(20, 20))
        self.clock = pygame.time.Clock()
        self.app_run = True

        # State management variables
        self.city_image = None
        self.show_image = False
        self.change_image()

    def change_image(self):
        cities = ["Berlin", "London", "Paris"]
        self.city_name = random.choice(cities)
        self.image_path = f"My Projects Until I WIN/My First Project/assets/{self.city_name}.png"
        
        try:
            self.city_image = pygame.image.load(self.image_path).convert_alpha()
        except pygame.error:
            # Bulletproof fallback if the asset file is missing
            self.city_name = pygame.Surface((300, 300))
            self.city_name.fill((100, 100, 100))

    def run(self):
        while self.app_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app_run = False

                if event.type == pygame.KEYDOWN and event.key == K_BACKSPACE:
                    self.show_image = not self.show_image
                    if self.show_image:
                        self.change_image()

            # 1. Clear frame buffer
            self.screen.fill((200, 200, 200))

            # 2. Blit assets in correct render order
            if self.show_image and self.city_image:
                self.screen.blit(self.city_image, (150, 150))

            self.t.draw(self.screen)

            # 3. Refresh display and tick clock
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    PygameApp().run()