#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

A = float(input('Digite o comprimento da primeira reta: '))
B = float(input('Digite o comprimento da segunda reta: '))
C = float(input('Digite o comprimento da terceira reta: '))

if A + B > C and B + C > A and A + C > B:
    print ('Pode formar um triângulo!')
else:
    print ('Não pode formar um triângulo!')
