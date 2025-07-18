#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print ('=-='*10)
print ('{:^30}'.format('Banco TaComKuNaVara'))
print ('=-='*10)
valortotal = int(input('Digite o valor que deseja sacar: R$'))
ced = 50
cont = 0
while True:
    if valortotal >= ced:
        cont += 1
        valortotal -= ced
    else:
        if cont > 0:    
            print (f'Total de {cont} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if valortotal == 0:
            break
        cont = 0
    
print ('=-='*10)
print ('Muito Obrigador por utilizar o banco TaComKuNaVara')
    
