import random


class Gene(object):
    """ Genetic Model Definition """

    def __init__(self, target):
        self.fitness = 0.0
        self.input = []
        self.mutate_rate = 0.1  # 10% rate to mutate
        self.target = target
        self.initalize_input()

    def initalize_input(self):
        for _ in range(len(self.target)):
            self.input.insert(0, chr(random.randint(32, 128)))

        # self.show_input()
        self.calculate_fitness()

    def calculate_fitness(self):
        # 각 모델에 따라 변경 될 부분.
        self.score = 0

        for x, y in enumerate(self.target):
            if self.input[x] == y:
                self.score += 1

        self.fitness = self.score/x
        self.fitness = self.fitness * 100
        self.fitness = int(self.fitness)
        """ 
        test code            
                             
        # print(self.fitness)
        # print(self.score)  
        """

    def show_input(self):
        print(self.input, end=" ")

    def get_input(self):
        # return input
        return self.input

    def mutate(self):
        # mutate input
        for x in range(len(self.input)):
            if self.mutate_rate > random.random():
                self.input[x] = chr(random.randint(32, 128))

        self.calculate_fitness()


class EvolveAlgorithm(object):
    """ evolve"""

    def __init__(self, own, other):
        self.own = own
        self.oth = other

    def cross_over(self):
        """ cross over """
        self.child = Gene(self.own.target)
        random_sector = random.randint(0, len(self.own.input)-1)

        for x in range(len(self.own.input)):
            if x < random_sector:
                self.child.input[x] = self.own.input[x]
            else:
                self.child.input[x] = self.oth.input[x]
        self.child.calculate_fitness()

        return self.child
