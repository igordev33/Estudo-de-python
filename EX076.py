#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular

print ('-'*30)
print (f'{'LISTAGEM DE PREÇOS':^30}')
print ('-'*30)
listagem = ('Picanha', 40.7,
            'Arroz', 7.89,
            'Macarrão', 3.45,
            'Pimenta', 7,
            'Love66', 35,
            'Extrato de tomate', 5.45)

for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<15}', end='')
    else:
        print(f'{listagem[pos]:.>15}')

