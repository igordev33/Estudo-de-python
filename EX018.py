#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
print ('Vamos calcular o seno, cosseno e tangente de um ângulo em graus!')
angulo_graus = int(input('Primeiro digite o ângulo: '))
angulo_radiano = math.radians(angulo_graus)
print('Cosseno: {}'.format(math.cos(angulo_radiano)))
print('Tangente: {}'.format(math.tan(angulo_radiano)))
print('Seno: {}'.format(math.sin(angulo_radiano)))