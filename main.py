# Mikhail Rudakov BS19-02

# imports
import ImageTest as imtest
from projectConstants import *
import toolbox
import os

# create folder to save results
if not os.path.exists(path_results):
    os.makedirs(path_results)

# create initial population
population = np.array([toolbox.Chromosome() for i in range(POPULATION_SIZE)])
print("ready to go")

# evolutionary algorithm main body
for i in range(EPOCHS + 1):
    # select best individuals to pass to the next generation without any changes
    # elitism technique. hof = hall of fame - best individuals
    hof = toolbox.hall_of_fame(population)
    # select individuals that survive to the next generation
    offspring = toolbox.select(population, len(population) - HOF_NUMBER)
    # perform pairwise crossover operator for survived individuals
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        # certain probability to change individuals
        if np.random.random() < P_CROSSOVER:
            toolbox.crossover(child1, child2)
            # set fitness to invalid state - means that we need to recalculate it
            child1.fitness_value = -1
            child2.fitness_value = -1
    # mutations for each individual in offspring
    for mutant in offspring:
        # perform mutation with certain probability
        if np.random.random() < P_MUTATION:
            toolbox.mutate(mutant)
            # set fitness value to be invalid - need to be recalculated
            mutant.fitness_value = -1
    # recalculate fitness if needed
    for entity in offspring:
        if entity.fitness_value == -1:
            entity.fitness()
    # update population - hall of fame and crossovered / mutated offspring
    population = np.concatenate((hof, offspring))
    # show results each 50 generations
    if i % 50 == 0:
        imtest.save_best_individual(population, i)
        imtest.save_population(population)
        print(i)
# the end of the algorithm
print('done.')
