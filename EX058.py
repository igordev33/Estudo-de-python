#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import choice

c = 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_sorteado = (choice(numeros))
print ('Vamos fazer uma brincadeira! Irei sortear um número de 1 a 10 e você tenta acertar.')
numero_escolhido = int(input('Digite o seu número: '))
while numero_sorteado != numero_escolhido :
    print ('Você errou! Tente novamente.')
    print ('-----------------------------------------------------------------------------')
    numero_escolhido = int(input('Digite o seu número: '))
    c = c + 1
print ('Você acertou!')
print ('Ao todo foram necessário {} tentativas.'.format(c))