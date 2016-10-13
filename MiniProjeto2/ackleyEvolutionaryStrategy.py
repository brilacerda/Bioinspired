from math import pi, cos, sqrt, exp
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

# 1. Qual será o tamanho da população?
# 2. Gostaria de inserir uma parcela dos 
# indivíduos com zeros em sua composição.
# 3. Usar também a recombinação feita por mhss no
# Mini-Projeto 1

class Candidate:
	def __init__(self, value=None):
		if value is None:
			# inicial aleatório
			self.value = [random()*30.0 - 15.0 for _ in range(n)]
		else:
			# filho de dois pais
			self.value = value

		# ao criar o candidato, já calcula o fitness
		self.calc_fitness()

	def calc_fitness(self):
		sum1, sum2 = 0, 0
		for i in self.value:
			sum1 += i**2
			sum2 += cos(c*i)

		self.fitness = -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + 1

		global minimum
		if self.fitness < minimum:
			minimum = self.fitness

	def cross(self, other, cut):
		new_value = self.value[:cut] + other.value[cut:]

		# mutação
		if random() < 0.1:
			new_value[randrange(n)] = random()*30.0 - 15.0

		return Candidate(new_value)

def main():
	global minimum
	minimum = 1e20

	# Inicialização aleatória
	global population
	population = [Candidate() for i in range(population_size)]

	for z in range(200):
		for y in range(100):
			recombination()
		survivorsSelection()
		print(minimum)

def recombination():
	'''
		intermediary
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
	global population
	global kids

	wholeCrew = population + kids
	wholeCrew.sort(key=lambda x: x.fitness)
	population = wholeCrew[:population_size]
	kids = []

if __name__ == "__main__":
	main()

