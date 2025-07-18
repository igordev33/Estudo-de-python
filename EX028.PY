#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
numeros = [1, 2, 3, 4, 5]
numerosorteado = (choice(numeros))
print ('Vamos fazer uma brincadeira! Irei sortear um número de 1 a 5 e se você acertar você ganha!')
numeroescolhido = int(input('Digite o seu número: '))
print ('O número sorteado foi: {}'.format(numerosorteado))
if numeroescolhido == numerosorteado:
    print ('Você ganhou!!!')
else:
    print('Que pena, você perdeu!')