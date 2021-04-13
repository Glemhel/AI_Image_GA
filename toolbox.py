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
    # mutate each position with certain probability, in average 1 is changed
    probability_mutation = 1 / float(p.data.shape[0])
    for i in range(p.data.shape[0]):
        if np.random.random() < probability_mutation:
            p.data[i] = np.random.normal(loc=p.data[i], scale=MUTATION_VARIANCE)


def crossover(p1: Chromosome, p2: Chromosome):
    # simulated binary crossover
    u = np.random.random()
    if u <= 0.5:
        beta = np.power((2 * u), 1.0 / (SBX_ETA + 1.0))
    else:
        beta = np.power(1 / (2 * (1 - u)), 1.0 / (SBX_ETA + 1.0))
    for i in range(p1.data.shape[0]):
        offspring1 = ((1 + beta) * p1.data[i] + (1 - beta) * p2.data[i]) / 2.0
        offspring2 = ((1 - beta) * p1.data[i] + (1 + beta) * p2.data[i]) / 2.0
        if np.random.random() <= 0.5:
            p1.data[i] = min(1, max(0, offspring1))
            p2.data[i] = min(1, max(0, offspring2))
        else:
            p1.data[i] = min(1, max(0, offspring2))
            p2.data[i] = min(1, max(0, offspring1))


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
