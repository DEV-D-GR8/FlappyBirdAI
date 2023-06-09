import pygame
import os

bottomPhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))

class Bottom:
    speed = 5
    width = bottomPhoto.get_width()
    image = bottomPhoto

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, window):
        window.blit(self.image, (self.x1, self.y))
        window.blit(self.image, (self.x2, self.y))
