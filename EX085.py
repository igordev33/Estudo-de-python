#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
dado = 0
for c in range (1, 8):
    dado = int(input(f'Digite o {c}° valor: '))
    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)
lista[0].sort()
lista[1].sort()
print (lista)
print (f'Valores impáres: {lista[1]}')
print (f'Valores pares: {lista[0]}')