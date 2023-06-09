from birdClass import Bird
from bottomClass import Bottom
from pipeClass import Pipe
from mainWindow import MainWindow as mw
import neat
import pygame
import pickle

floorDimension = 730
windowWidth = 600
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))

gen = 0
class BirdTraining:
    
    def trainBirds(genomes, config):
        
        global window, gen
        win = window
        gen += 1
        birds = []
        genos = []
        neuralNetworks = []
        for _, genome in genomes:
            genome.fitness = 0  
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            neuralNetworks.append(net)
            birds.append(Bird(230,350))
            genos.append(genome)

        base = Bottom(floorDimension)
        pipes = [Pipe(700)]
        score = 0

        clock = pygame.time.Clock()

        run = True
        while run and len(birds) > 0:
            clock.tick(500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
                    break

            pipeIndex = 0
            if len(birds) > 0:
                if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].pipeTop.get_width():  
                    pipeIndex = 1                                                                 

            for x, bird in enumerate(birds):
                genos[x].fitness += 0.1
                bird.move()
                output = neuralNetworks[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipeIndex].height), abs(bird.y - pipes[pipeIndex].bottom)))
                if output[0] > 0.5: 
                    bird.jump()

            base.move()

            rem = []
            addPipe = False
            for pipe in pipes:
                pipe.move()
                for bird in birds:
                    if pipe.collide(bird, win):
                        genos[birds.index(bird)].fitness -= 1
                        neuralNetworks.pop(birds.index(bird))
                        genos.pop(birds.index(bird))
                        birds.pop(birds.index(bird))

                if pipe.x + pipe.pipeTop.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    addPipe = True

            if addPipe:
                score += 1
                for genome in genos:
                    genome.fitness += 5
                pipes.append(Pipe(windowWidth))

            for r in rem:
                pipes.remove(r)

            for bird in birds:
                if bird.y + bird.image.get_height() - 10 >= floorDimension or bird.y < -50:
                    neuralNetworks.pop(birds.index(bird))
                    genos.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            mw.drawWindow(window, birds, pipes, base, score, gen, pipeIndex)

            if score > 1000:
                pickle.dump(neuralNetworks[0],open("winner.pkl", "wb"))
                break
