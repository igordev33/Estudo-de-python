#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Bahia', 'Botafogo', 'Ceará SC', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Mirassol', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco Da Gama', 'EC Vitória')

print ('Relatório diário do Campeonato Brasileiro de futebol')
print ('=-='*20)
print ('Os 5 primeiros times na colocação do campeonato brasileiro são: ')

#Mostrando os 5 primeiros times.
for c in range (0, 5):
    print (f'O {c + 1}° colocado é: {times[c]}')
print ('=-='*20)

#Mostrando os 4 últimos times.
print ('Os últimos 4 colocados e com risco de rebaixamento são: ')
for c in range (4, 0, -1):
    print (f'O {21 - c}° colocado é {times[-c]}')
print ('=-='*20)

#Mostrando os times em ordem alfabética.
print ('A seguir uma lista com os times em ordem alfabética: ')
print (sorted(times))
print ('=-='*20)

#Pedir para escolher um time e retornar a posição do mesmo no campeonato brasileiro.
time_escolhido = str(input('Digite o nome de um time e te direi em que posição ele está: ')).strip().title()
if time_escolhido in times:
    posicao = times.index(time_escolhido)
    print (f'O time {time_escolhido} está na posição {posicao + 1}')
else:
    print ('Esse time não está na colocação do campeonato brasileiro de futebol.')

