from birdClass import Bird
from bottomClass import Bottom
from pipeClass import Pipe
from manualScreen import ManualWindow as mw
from collisionScreen import Collision as col
import neat
import pygame
import pickle

floorDimension = 730
windowWidth = 600
windowHeight = 800

window = pygame.display.set_mode((windowWidth, windowHeight))

class PlayManual:
    
    def playerInControl():
        
        win = window
        bird = Bird(300, 250)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        score = 0

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        bird.jump()
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()                                                              
            if bird.y > 700:
                while True:
                    col.aiCollided(score)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            pygame.quit()
                            quit()
            bird.move()

            base.move()

            rem = []
            addPipe = False
            for pipe in pipes:
                pipe.move()
                
                if pipe.collide(bird, win):
                    while True:
                        col.aiCollided(score)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                pygame.quit()
                                quit()

                if pipe.x + pipe.pipeTop.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    addPipe = True

            if addPipe:
                score += 1
                pipes.append(Pipe(windowWidth))

            for r in rem:
                pipes.remove(r)

            
            mw.drawManualPlayWindow(window, bird, pipes, base, score)
            
    def main():

        run = True
        go = False
        while run:
            mw.drawManualWindow()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    go = True
                    run = False
        while go:
            PlayManual.playerInControl()
