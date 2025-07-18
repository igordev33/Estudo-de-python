#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

random_numbers = tuple(random.sample(range(1, 100), 5))

print (random_numbers)
print (f'O maior valor dentro da tupla é: {max(random_numbers)}')
print (f'O menor valor dentro da tupla é: {min(random_numbers)}')