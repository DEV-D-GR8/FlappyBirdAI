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

class Train:
    def startTraining():
        win = window
        bird = Bird(250, 150)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)
        base.draw(win)
        bird.draw(win)
        scoreLabel = ef.render("Press any key",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 160, 220))
        scoreLabel = ef.render("to start training ",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 120, 300))
        pygame.display.update()
        
        