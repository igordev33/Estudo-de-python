#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
listapar = list()
listaimpar = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    print ('Numero adicionado com sucesso...')
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
print('=-='*30)
print (f'Essa é a lista que voce gerou: {lista}')
print (f'Essa é uma lista com somente os numero pares que você digitou: {listapar}')
print (f'Essa é uma lista com somente os numeros impares que você digitou: {listaimpar}')
