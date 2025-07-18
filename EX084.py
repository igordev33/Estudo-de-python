#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.    
# B) Uma listagem com as pessoas mais pesadas.  
# C) Uma listagem com as pessoas mais leves.

pessoas = []
pessoas_pesadas = []
pessoas_leves = []
dado = []
continuar = ''
totpessoas = pesados = leves = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    dado.append(str(input('Sexo [F/M]: ')).upper())
    while dado[2] not in ('F', 'M'):
        print ('Opção Inválida...')
        del dado[2]
        dado.append(str(input('Sexo [F/M]: ')).upper())
    if dado[2] == 'F':
        if dado[1] > 65:
            pessoas_pesadas.append(dado[:])
        else:
            pessoas_leves.append(dado[:])
    else:
        if dado[1] >80:
            pessoas_pesadas.append(dado[:])
        else:
            pessoas_leves.append(dado[:])
    pessoas.append(dado[:])
    dado.clear()
    totpessoas += 1
    continuar = input('Deseja continuar [S/N]: ')
    print ('-'*30)
    if continuar in 'Nn':
        break
print ('=-='*30)
print (f'Total de pessoas: {totpessoas}')
print (f'Lista completa: {pessoas}')
print (f'Lista com pessoas mais pesadas: {pessoas_pesadas}')
print (f'Lista com as pessoas mais leves: {pessoas_leves}')


