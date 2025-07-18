#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

soma = mais1000 = cont = maisbarato =  0
nomemaisbarato = ''

while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preço = float(input(('Preço do produto: R$')))
    cont += 1
    soma += preço
    if preço >= 1000:
        mais1000 += 1
    if cont == 1:
        maisbarato = preço
        nomemaisbarato = nome
    else:
        if maisbarato > preço:
            maisbarato = preço
            nomemaisbarato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print ('=-='*30)
    if resp == 'N':
        break
print (f'Total gasto na compra: R${soma:.2f}')
print (f'Ao todo {mais1000} produtos custam mais de R$1000.')
print (f'O produto mais barato é {nomemaisbarato} no valor de R${maisbarato}.')


    
    

