#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('Cateto oposto: {}'.format(cateto_oposto))
print('Cateto adjacente: {}'.format(cateto_adjacente))
print('Hipotenusa: {:.3}'.format(hipotenusa))
