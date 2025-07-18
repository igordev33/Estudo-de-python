#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = [int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: '))]
print (lista)
print (f'O maior valor dentro dessa lista é {max(lista)} na posição {lista.index(max(lista))}')
print (f'O menor valor dentro dessa lista é {min(lista)} na posição {lista.index(min(lista))}')