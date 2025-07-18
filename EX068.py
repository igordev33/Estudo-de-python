#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0
print ('='*40)
print ('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    print ('='*40)
    nmachine = random.choice(lista)
    n = int(input('Digite o seu número: '))
    r = nmachine + n
    pi = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    print (f'Minha esocolha: {nmachine}')
    if pi == 'P':
        if r % 2 == 0:
            print ('Você ganhou!')
            c += 1
        else:
            print ('Você perdeu!')
            break
    elif pi == 'I':
        if r % 2 != 0:
            print ('Você ganhou!')
            c+=1
        else:
            print ('Você perdeu!')
            break
    else:
        print ('OPÇÃO INVÁLIDA')
print (f'Você ganhou {c} vezes!')


