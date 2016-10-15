from math import pi, cos, sqrt, exp, fabs
from random import random, randrange, sample

a = 20
b = 0.2
c = 2*pi
n = 6
x = 3
population_size = 200
population = []
kids = []
minimum = 1e20


# 3. Usar também a recombinação feita por mhss no
# Mini-Projeto 1

class Candidate:
	def __init__(self, value=None):
		if value is None:
			# Aleatory initialization
			self.value = [random()*30.0 - 15.0 for _ in range(n)]
		else:
			# 2 parents child
			self.value = value

		# fitness is always calculated, even when the candidate is created 
		self.calc_fitness()

	def calc_fitness(self):
		sum1, sum2 = 0, 0
		for i in self.value:
			sum1 += i**2
			sum2 += cos(c*i)

		self.fitness = -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + 1

		global minimum
		# Absolute value of the fitness
		if fabs(self.fitness) < minimum:
			minimum = self.fitness

	def cross(self, other, cut):
		new_value = self.value[:cut] + other.value[cut:]

		# mutation
		if random() < 0.1:
			new_value[randrange(n)] = random()*30.0 - 15.0

		return Candidate(new_value)

def main():
	global minimum
	minimum = 1e20

	# Aleatory initialization
	global population

	# Aleatory sample
	population = [Candidate() for i in range(population_size)]
	# 200 generations
	for z in range(200):
		# 100 kids generated
		for y in range(100):
			recombination()
		survivorsSelection()
		print(z, "generation", minimum)

def recombination():
	'''
		2 aleatory parents and an aleatory cut
		The best out of the 2 children
	'''
	inds = sample(population, 2)
	cut = randrange(1, n)
	
	child1 = inds[0].cross(inds[1], cut)
	child2 = inds[1].cross(inds[0], cut)

	if child1.fitness < child2.fitness:
		kids.append(child1)
	else:
		kids.append(child2)

def survivorsSelection():
	'''
		200 bests between the population and children 
	'''
	global population
	global kids

	wholeCrew = population + kids
	wholeCrew.sort(key=lambda x: x.fitness)
	population = wholeCrew[:population_size]
	kids = []

if __name__ == "__main__":
	main()