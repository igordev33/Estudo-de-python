#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
c = 0
soma = 0
n = int(input('Digite um número: [999 para parar] '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número: [999 para parar] '))
print ('A quantidade de valors digitados foi de {} e a soma entre eles é {}'.format(c, soma))

