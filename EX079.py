#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = [int(input ('Digite um número: '))]

for n in range (0, 4):    
    add = int(input('Digite outro número: '))
    if add not in lista:
        lista.append(add)
print (lista)
lista.sort()
print (lista)
