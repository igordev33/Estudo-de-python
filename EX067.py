#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('Este programa tem como objetivo você aprender a tabuada. Digite um número e te mostrarei a tabuada dele, para parar é só digitar um número negativo.')
while True:
    n = int(input('Seu número: '))
    if n < 0:
        break
    for c in range (1, 11):
        print (f'{n} x {c} = {n * c}')
print ('Programa encerrado.')
