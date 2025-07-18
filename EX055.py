#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = float(0)
menor = float(999999999999999999999999999)
for c in range (1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print ('O maior peso digitado foi de: {}'.format(maior))
print ('O menor peso digitado foi de: {}'.format(menor))