import numpy as np
from projectConstants import *
from copy import deepcopy
import ImageTest as imtest


class Chromosome:

    def __init__(self, data=None):
        if data is None:
            self.data = imtest.generateRandomImageData(POLYGONS_NUMBER)
        else:
            self.data = data
        self.fitness_value = imtest.fitness_function(self.data)

    def __repr__(self):
        return imtest.dataToImage(self.data)

    def fitness(self):
        self.fitness_value = imtest.fitness_function(self.data)
        return self.fitness_value


def mutate(p: Chromosome):
    mutation_position = np.random.randint(0, p.data.shape[0])
    # p.data[mutation_position] = max(0, min(
    #     np.random.normal(loc=p.data[mutation_position],scale=MUTATION_VARIANCE), 1
    # ))
    p.data[mutation_position] = np.random.random()


def crossover(p1: Chromosome, p2: Chromosome):
    # simulated binary crossover
    u = np.random.random()
    if u <= 0.5:
        beta = np.power((2 * np.random.random()), 1.0 / (SBX_ETA + 1.0))
    else:
        beta = np.power(1 / (2 * (1 - u)), 1.0 / (SBX_ETA + 1.0))
    for i in range(p1.data.shape[0]):
        if np.random.random() <= 0.5:
            offspring1 = ((1 + beta) * p1.data[i] + (1 - beta) * p2.data[i]) / 2.0
            offspring2 = ((1 - beta) * p1.data[i] + (1 + beta) * p2.data[i]) / 2.0
            p1.data[i] = np.median([0, 1, offspring1])
            p2.data[i] = np.median([0, 1, offspring2])


def select(population, offspring_size, method='tournament'):
    if method == 'tournament':
        selected = np.empty(offspring_size, dtype=object)
        for i in range(offspring_size):
            participants = np.random.choice(len(population), size=TOURNAMENT_SIZE, replace=False)
            winner = min(participants, key=lambda x: population[x].fitness_value)
            selected[i] = deepcopy(population[winner])
        return selected
    return np.copy(population[:offspring_size])


def hall_of_fame(population, best_size=HOF_NUMBER):
    population_fitness = np.array([population[i].fitness_value for i in range(population.shape[0])])
    hof = np.argsort(population_fitness)[:best_size]
    hof = np.array([population[i] for i in hof])
    return hof
