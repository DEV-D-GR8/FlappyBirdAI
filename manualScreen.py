import pygame
import os
from bottomClass import Bottom
from pipeClass import Pipe
from birdClass import Bird

windowWidth = 600
windowHeight = 800
pygame.display.init()
window = pygame.display.set_mode((windowWidth, windowHeight))
floorDimension = 730
backgroundPhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))
pygame.font.init()
sf = pygame.font.SysFont("comicsans", 50)
ef = pygame.font.SysFont("comicsans", 30)
play = False
class ManualWindow:
    def drawManualWindow():
        win = window
        bird = Bird(250, 310)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        score = 0
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)
        base.draw(win)
        bird.draw(win)

        scoreLabel = sf.render("Score: " + str(score),1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 220, 10))
        scoreLabel = sf.render("System ready!",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 140, 220))
        scoreLabel = sf.render("Press any key to play.",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 60, 370))
        pygame.display.update()
        
    def drawManualPlayWindow(window, bird, pipes, bottom, score):
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)

        bottom.draw(window)
        bird.draw(window)
        scoreLabel = sf.render("Score: " + str(score),1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 15, 10))
        pygame.display.update()