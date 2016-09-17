from random import *

toBinary = {
	'0' : '000',
	'1' : '001',
	'2' : '010',
	'3' : '011',
	'4' : '100',
	'5' : '101',
	'6' : '110',
	'7' : '111'
}

# Criar a representação da estrutura ex.:
# [000, 001, 010, 011, 100, 101, 110, 111]
population = {}
sample = ['000', '001', '010', '011', '100', '101', '110', '111']
print (population)

def checkIndividual(ind):
	return ind

# def individualToBinary(ind):
# 	temp = []
# 	for i in range(8):
# 		temp[i] = toBinary[str(ind[i])]
# 		print (temp[i])

# 	return temp


# Inicialização aleatória
# Geração de 100 indivíduos
for i in range(10):
	shuffle(sample)

	# Avaliação da solução
	# if checkIndividual(sample)
	# 	print ("Solution found at %s" % i, temp)
	# 	break

	population[i] = sample;
	print (sample)


# convertendo pra fenótipo
# print int('00100001', 2)
