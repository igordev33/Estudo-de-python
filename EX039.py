#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime
print ('Alistamento Militar TaComKuNoCano')
nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = int(datetime.now().year)
idade = ano_atual - nascimento

if idade == 18:
    print ('Está na hora de se alistar! Venha para o campo militar TaComKuNoCano.')
elif idade > 18:
    print ('Já se passaram {} anos do seu tempo de alistamento. Se aliste agora para naõ ser preso!'.format(idade - 18))
elif idade < 18 :
    print ('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
