from math import pi, cos, sqrt, exp
from random import random

a = 20
b = 0.2
c = 2*pi
n = 6
x = 3
population_size = 50
convergedAt = []
population = []
minimum = 100
# Qual será o tamanho da população?

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

def calculateAckley(individual):
	sum1 = 0
	sum2 = 0

	for ind in individual:
		sum1 += ind**2
		sum2 += cos(c*ind)

	return -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + 1