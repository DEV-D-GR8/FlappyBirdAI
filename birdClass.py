import neat
import os
import time
import random
import pygame

b1 = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png")))
b2 = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png")))
b3 = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))

birdPhotos = [b1, b2, b3]

class Bird:
    bp = birdPhotos
    animationDuration = 5
    rotationSpeed = 20
    maxRotation = 25
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCount = 0
        self.imageCount = 0
        self.speed = 0
        self.height = self.y
        self.image = self.bp[0]
        
    def jump(self):
        self.speed = -10.5
        self.tickCount = 0
        self.height = self.y
        
    def move(self):
        self.tickCount += 1
        d = self.speed * self.tickCount + 1.5 * self.tickCount**2
        
        if d>=16:
            d = 16
            
        if d<0:
            d -= 2
            
        self.y = self.y + d
        
        if d<0 or self.y <self.height + 50:
            if self.tilt <self.maxRotation:
                self.tilt = self.maxRotation
        else:
            if self.tilt > -90:
                self.tilt -= self.rotationSpeed
                
    def draw(self, window):
        self.imageCount += 1
        
        if self.imageCount <self.animationDuration:
            self.image = self.bp[0]
        elif self.imageCount <self.animationDuration*2:
            self.image = self.bp[1]
        elif self.imageCount <self.animationDuration*3:
            self.image = self.bp[2]
        elif self.imageCount <self.animationDuration*4:
            self.image = self.bp[1]
        elif self.imageCount == self.animationDuration*4 + 1:
            self.image = self.bp[0]
            self.imageCount = 0
            
        if self.tilt <= -80:
            self.image = self.bp[1]
            self.imageCount = self.animationDuration*2
            
        rotatedImage = pygame.transform.rotate(self.image, self.tilt)
        newRect = rotatedImage.get_rect(center=self.image.get_rect(topleft = (self.x, self.y)).center)
        window.blit(rotatedImage, newRect.topleft)
        
    def getMask(self):
        return pygame.mask.from_surface(self.image)