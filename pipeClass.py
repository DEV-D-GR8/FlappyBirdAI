import pygame
import random
import os

pipePhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))

class Pipe():
    gap = 200
    speed = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0

        self.pipeTop = pygame.transform.flip(pipePhoto, False, True)
        self.pipeBottom = pipePhoto

        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.pipeTop.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.speed

    def draw(self, window):
        window.blit(self.pipeTop, (self.x, self.top))
        window.blit(self.pipeBottom, (self.x, self.bottom))


    def collide(self, bird, win):
        birdMask = bird.getMask()
        topMask = pygame.mask.from_surface(self.pipeTop)
        bottomMask = pygame.mask.from_surface(self.pipeBottom)
        topOff = (self.x - bird.x, self.top - round(bird.y))
        bottomOff = (self.x - bird.x, self.bottom - round(bird.y))

        bottomCollisionPoint = birdMask.overlap(bottomMask, bottomOff)
        topCollisionPoint = birdMask.overlap(topMask,topOff)

        if bottomCollisionPoint or topCollisionPoint:
            return True

        return False