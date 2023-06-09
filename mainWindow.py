import pygame
import os

windowWidth = 600
windowHeight = 800
backgroundPhoto = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))
pygame.font.init()
sf = pygame.font.SysFont("comicsans", 50)
ef = pygame.font.SysFont("comicsans", 70)
class MainWindow:
    def drawWindow(window, birds, pipes, bottom, score, gen, pipeIndex):
        
        if gen == 0:
            gen = 1
        window.blit(backgroundPhoto, (0,0))

        for pipe in pipes:
            pipe.draw(window)

        bottom.draw(window)
        lines = True
        for bird in birds:
            if lines:
                try:
                    pygame.draw.line(window, (255,0,0), (bird.x+bird.image.get_width()/2, bird.y + bird.image.get_height()/2), (pipes[pipeIndex].x + pipes[pipeIndex].pipeTop.get_width()/2, pipes[pipeIndex].height), 5)
                    pygame.draw.line(window, (255,0,0), (bird.x+bird.image.get_width()/2, bird.y + bird.image.get_height()/2), (pipes[pipeIndex].x + pipes[pipeIndex].pipeBottom.get_width()/2, pipes[pipeIndex].bottom), 5)
                except:
                    pass
            bird.draw(window)

        scoreLabel = sf.render("Score: " + str(score),1,(255,255,255))
        window.blit(scoreLabel, (windowWidth - scoreLabel.get_width() - 15, 10))

        genLabel = sf.render("Generation: " + str(gen-1),1,(255,255,255))
        window.blit(genLabel, (10, 10))

        aliveLabel = sf.render("Alive: " + str(len(birds)),1,(255,255,255))
        window.blit(aliveLabel, (10, 50))

        pygame.display.update()