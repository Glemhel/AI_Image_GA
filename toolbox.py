import numpy as np
from projectConstants import *


def select(population, offspring_size, method='tournament'):
    population_fitness = np.empty(len(population))
    for j in range(len(population)):
        population_fitness[j] = population[j].fitness()
    if method == 'tournament':
        selected = np.array([])
        for i in range(offspring_size):
            participants = np.random.choice(len(population), size=TOURNAMENT_SIZE, replace=False)
            winner = min(participants, key=lambda x: population_fitness[x])
            selected = np.append(selected, population[winner])
        return selected
    return np.copy(population[:offspring_size])
