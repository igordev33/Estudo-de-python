#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
ano_atual = datetime.now().year
s = 0
sn = 0
for c in range (1, 8):
    bornyear = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    year = ano_atual - bornyear
    if year >= 21:
        s = s + 1
    else:
        sn = sn + 1
print ('Foram digitados ao todo {} idades que atingiram a maioridade.'.format(s))
print ('Foram digitados ao todo {} idades que NÃO atingiram a maioridade.'.format(sn))