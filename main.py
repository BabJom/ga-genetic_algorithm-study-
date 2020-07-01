"""
Genetic algorithm 
Create 
 
2020 07 01 
success!!

"""
import os
import random
from Genome import Gene
from Genome import EvolveAlgorithm


def sort_data(data):
    data.sort(key=lambda obj: obj.fitness, reverse=True)


def main(target):
    """ main loop """
    population_gene = []
    gene_count = 150

    for _ in range(gene_count):
        new_gene = Gene(target)
        if new_gene.fitness != 0:
            population_gene.append(new_gene)

    sort_data(population_gene)
    calculate_list = []

    status = True
    while status:
        for x in population_gene:
            for _ in range(x.fitness):
                calculate_list.append(x)
        for _ in range(100):
            rand_one = random.choice(calculate_list)
            rand_two = random.choice(calculate_list)

            evolve = EvolveAlgorithm(rand_one, rand_two)
            child = evolve.cross_over()
            child.mutate()
            population_gene.append(child)

        sort_data(population_gene)
        population_gene = population_gene[:20]

        for x in population_gene:
            if x.score == len(child.input):
                status = False

    sort_data(population_gene)
    print(population_gene[0].input)


if __name__ == "__main__":
    """
     if main execute file 
     run this
    """
#    target = "To be or not to be."
    target = input("input data")

    main(target)
