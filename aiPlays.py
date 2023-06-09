from birdClass import Bird
from bottomClass import Bottom
from pipeClass import Pipe
from playingWindow import PlayWindow as pw
from collisionScreen import Collision as col
import neat
import pygame
import pickle

floorDimension = 730
windowWidth = 600
windowHeight = 800

window = pygame.display.set_mode((windowWidth, windowHeight))

class PlayWithAI:
    
    def aiInControl():
        
        win = window
        neuralNetwork = pickle.load(open('winner.pkl', 'rb'))
        bird = Bird(300, 250)
        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        score = 0

        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                    break

            pipeIndex = 0
            if len(pipes) > 1 and bird.x > pipes[0].x + pipes[0].pipeTop.get_width():  
                pipeIndex = 1                                                                 

            bird.move()
            output = neuralNetwork.activate((bird.y, abs(bird.y - pipes[pipeIndex].height), abs(bird.y - pipes[pipeIndex].bottom)))
            if output[0] > 0.5: 
                bird.jump()

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

            
            pw.drawPlayWindow(window, bird, pipes, base, score)
            
    def main():

        run = True
        go = False
        while run:
            pw.drawStartWindow()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    go = True
                    run = False
        while go:
            PlayWithAI.aiInControl()