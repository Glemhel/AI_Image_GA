# Mikhail Rudakov

from projectConstants import *
from copy import deepcopy
import ImageTest as imtest


# Chromosome - individual in my population
# it is represented with array of numbers from 0 to 1, that are scaled to the desired value only at
# drawing time
# it has EMOJIS_NUMBER * EMOJIS_REPETITIONS * ENTRY_SIZE numbers in it.
# first EMOJIS_REPETITIONS * ENTRY_SIZE numbers describe positions and colors of
# first emoji in the array for drawing (it appears EMOJIS_REPETITIONS times),
# next EMOJIS_REPETITIONS * ENTRY_SIZE - second, etc.
class Chromosome:

    # create individual
    def __init__(self):
        self.data = create_individual_data()
        self.fitness_value = fitness_function(self.data)

    def __repr__(self):
        return imtest.dataToImage(self.data)

    # calculate fitness
    def fitness(self):
        self.fitness_value = fitness_function(self.data)
        return self.fitness_value


# create data array for individual
def create_individual_data():
    return np.random.random(ENTRY_SIZE * EMOJI_REPETITIONS * EMOJIS_NUMBER)


# calculate fitness function for the individual
def fitness_function(data):
    return imtest.imageDifferenceFromSample(data)


# mutation operator for evolutionary algorithm
def mutate(p: Chromosome):
    # mutate each position with certain probability, in average 1 number is changed
    probability_mutation = 1 / float(p.data.shape[0])
    for i in range(p.data.shape[0]):
        if np.random.random() < probability_mutation:
            # generate new number in the neighbourhood of previous value - normal distribution
            p.data[i] = np.random.normal(loc=p.data[i], scale=MUTATION_VARIANCE)


# crossover operator for evolutionary algorithm
def crossover(p1: Chromosome, p2: Chromosome):
    # simulated binary crossover technique is utilized
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


# selection operator for evolutionary algorithm
def select(population, offspring_size, method='tournament'):
    # tournament selection is used
    if method == 'tournament':
        selected = np.empty(offspring_size, dtype=object)
        # for each of n rounds
        for i in range(offspring_size):
            # TOURNAMENT_SIZE individuals are selected randomly and uniformly
            participants = np.random.choice(len(population), size=TOURNAMENT_SIZE, replace=False)
            # best of them in terms of fitness is passed to the next population
            winner = min(participants, key=lambda x: population[x].fitness_value)
            selected[i] = deepcopy(population[winner])
        return selected
    return np.copy(population[:offspring_size])


# generate hall of fame for the current population
def hall_of_fame(population, best_size=HOF_NUMBER):
    population_fitness = np.array([population[i].fitness_value for i in range(population.shape[0])])
    # select best_size individuals that are best in terms of fitness
    hof = np.argsort(population_fitness)[:best_size]
    hof = np.array([population[i] for i in hof])
    return hof
