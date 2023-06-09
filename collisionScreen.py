import pygame
import os
from bottomClass import Bottom
from pipeClass import Pipe
from birdClass import Bird

windowWidth = 600
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
floorDimension = 730
backgroundPhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))
pygame.font.init()
sf = pygame.font.SysFont("comicsans", 50)
ef = pygame.font.SysFont("comicsans", 50)

class Collision:
    def aiCollided(score):
        win = window
        bird = Bird(250, 310)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)
        base.draw(win)
        bird.draw(win)
        scoreLabel = ef.render("Game Over!",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 190, 220))
        scoreLabel = ef.render("Score: "+str(score),1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 210, 370))
        pygame.display.update()
        