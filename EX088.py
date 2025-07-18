#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
game = []
list_of_games = []
data = 0

print('=-=' * 10)
print(f'{'GERADOR DE JOGOS DA MEGASENA':^30}')
print('=-=' * 10)
number_of_games = int(input('Digite quantos jogos deseja jogar: '))
for i in range (1, number_of_games + 1):
    for c in range (0, 6):
        data = random.randint(1, 60)
        while data in game:
            data = random.randint(1, 60)
        game.append(data)
        game.sort()
    print (f'Resultado do {i}º jogo: {game}')
    list_of_games.append(game[:])
    game.clear()
print('=-=' *10)
print ('Lista com todos os jogos: ')
print (list_of_games)
