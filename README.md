# Bioinspired

**_Made in python version 3.4.3_**

Especificação Mini-projeto 2 – Estratégia Evolutiva
----------------------------------

Desenvolvimento de um Algoritmo Evolucionário (Estratégia Evolutiva) para a determinação do ponto de mínimo global da [Função de Ackley](https://www.sfu.ca/~ssurjano/ackley.html)
Considere n = 30 e -15 ≤ xi ≤ 15.

Cada equipe, de no máximo de 3 integrantes, deverá implementar um Algoritmo
Evolutivo (Estratégia Evolutiva) em qualquer linguagem de programação. Além da implementação, a equipe deverá gerar um relatório descrevendo a sua implementação, dando ênfase nos tópicos:
1. Descrição esquemática do algoritmo implementado;
2. Descrição dos processos de:
* Representação das soluções (indivíduos)
* Função de Fitness
* População (tamanho, inicialização, etc)
* Processo de seleção
* Operadores Genéticos (Recombinação e Mutação)
* Processo de seleção por sobrevivência
* Condições de término do Algoritmo Evolucionário
3. Descrição dos resultados experimentais

** Compare com uma modificação da própria Estratégia Evolutiva, ou com um Algoritmo Genérico (Real)


Especificação Mini-projeto – 8 rainhas
-----------------------------------

### Primeira parte:
* Representação (genótipo): string de bits
* Recombinação: “cut-and-crossfill” crossover
* Probabilidade de Recombinação: 90%
* Mutação: troca de genes
* Probabilidade de Mutação: 40%
* Seleção de pais: ranking - Melhor de 2 de 5 escolhidos aleatoriamente
* Seleção de sobreviventes: substituição do pior
* Tamanho da população: 100
* Número de filhos gerados: 2
* Inicialização: aleatória
* Condição de término: Encontrar a solução, ou 10.000 avaliações de fitness
* Fitness?

### Segunda parte:
#### Implementar possíveis melhorias mudando:
* Representação
* Recombinação 
* Mutação
* Seleção de pais – roleta?
* Seleção de sobreviventes: geracional ou substituição do pior
* Tamanho da população: 10? 30? 50? 70? 120? 200?
* O fitness pode ser melhorado?
