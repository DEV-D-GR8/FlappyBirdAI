import os
import pygame
from neuralNetwork import NeuralNetwork as nn
from playingWindow import PlayWindow as pw
from aiPlays import PlayWithAI as ai
from startTrainingScreen import Train as t
from manual import PlayManual as pm
from bottomClass import Bottom
from pipeClass import Pipe
from birdClass import Bird


pygame.display.set_caption("Flappy Bird")
windowWidth = 600
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
floorDimension = 730
backgroundPhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))
pygame.font.init()
sf = pygame.font.SysFont("comicsans", 50)
ef = pygame.font.SysFont("comicsans", 30)

def choose() -> int:
    keyc = 0
    run = True
    while run:
        win = window
        bird = Bird(250, 170)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)
        base.draw(win)
        bird.draw(win)
        scoreLabel = sf.render("Welcome!",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 200, 25))
        scoreLabel = ef.render("Press '1' for manual gameplay",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 90, 320))
        scoreLabel = ef.render("Press '2' to train AI and play",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 90, 370))
        scoreLabel = ef.render("Press '3' to play with pre-trained AI",1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 55, 420))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    keyc = 1
                elif event.key == pygame.K_2:
                    keyc = 2
                elif event.key == pygame.K_3:
                    keyc = 3
                else:
                    keyc = 2
                run = False
                break

    return keyc

if __name__ == '__main__':
    
    choice = choose()
    if choice == 1:
        pm.main()
    elif choice == 3:
        ai.main()
    else:
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'configFile.txt')
        
        r = True
        go = False
        while r:
            t.startTraining()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    go = True
                    r = False
        while go:
            nn.run(config_path)
            break
        ai.main()