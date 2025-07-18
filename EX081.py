#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.            Depois disso mostre:                                                                                               A) Quantos números foram digitados.                                                                                            B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    N = int(input('Digite um número: '))
    lista.append(N)
    print ('Numero adicionado a lista...')
    resp = str(input('Deseja continuar [S/N]: '))
    print ('=-='*30)
    if resp in 'nN':
        break

print (f'Ao todo foram digitados {len(lista)} números.')

lista.sort(reverse= True)
print (f'Lista ordenada de forma decrescente: {lista}')

if 5 in lista:
    print(f'Ao todo o número 5 apareceu {lista.count(5)} vezes')
else:
    print ('O número 5 não apareceu na lista')