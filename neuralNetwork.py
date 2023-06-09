import neat
from trainingBirds import BirdTraining as bt 
import pickle
class NeuralNetwork:
    def run(config_file):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_file)

        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        winner = p.run(bt.trainBirds, 50)

        print('\nBest genome:\n{!s}'.format(winner))
        