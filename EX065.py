#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

r = 'S'
soma = n = maior = c = 0
menor = 99999999999999999999999999999999999999999999999999999999999999
while r == 'S':
    c += 1
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()
media = float(soma / c)
print ('A média entre todos os números digitados é: {}'.format(media))
print ('Maior número digitado: {}'.format(maior))
print ('Menor número digitado: {}'.format(menor))

    