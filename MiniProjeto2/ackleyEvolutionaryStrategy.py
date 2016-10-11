from math import pi, cos, sqrt, exp
from random import random, randrange

a = 20
b = 0.2
c = 2*pi
n = 6
x = 3
population_size = 200
convergedAt = []
population = []
kids = []
minimum = 100

# 1. Qual será o tamanho da população?
# 2. Gostaria de inserir uma parcela dos 
# indivíduos com zeros em sua composição.
# 3. Usar também a recombinação feita por mhss no
# Mini-Projeto 1


def main():
	minimum = 100
	# Inicialização aleatória
	for i in range(population_size):
		sample = generateIndividual()

		# Avaliação da solução
		fx = calculateAckley(sample)
		if fx < minimum:
			minimum = fx
			print ("f(x) = ", fx)
		if not fx:
			population.append(sample)
			print ("f(x)=0 when ", sample)
			convergedAt.append(i)
		else:
			population.append(sample)
			#print ("ind #%s "%i, sample)

	for z in range(200):
		if not 200%100:
			survivorsSelection()

		recombination()

def generateIndividual():
	individual = []
	for i in range(n):
		v = random()*10
		if v <= 30:
			v-=15
		elif v <= 60:
			v-=45
		elif v <= 90:
			v-=75
		else:
			v = ((v-90)*3)-15
		individual.append(v)
	return individual

# def getMinimum(fx):
# 	if fx < minimum:
# 		minimum = fx
# 		print ("f(x) = ", fx)

def calculateAckley(individual):
	sum1 = 0
	sum2 = 0

	for ind in individual:
		sum1 += ind**2
		sum2 += cos(c*ind)
	fx = -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + 1
	# getMinimum(fx)
	return fx

def recombination():
	'''
		intermediary
	'''
	child1 = []
	child2 = []
	ind1 = population[randrange(population_size)]
	ind2 = population[randrange(population_size)]
	cut = randrange(n)

	for i in range(n):
		if i <= cut:
			child1.append(ind1[i])
			child2.append(ind2[i])
		else:
			child1.append(ind2[i])
			child2.append(ind1[i])
	
	if calculateAckley(child1) < calculateAckley(child2):
		kids.append(child1)
	else:
		kids.append(child2)

def survivorsSelection():
	wholeCrew = population + kids
# 	wholeCrew.sort()
# 	population = wholeCrew[0:199]
#	kids = []