#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

name = str(input('Digite um nome: '))
print ('Nome: {}'.format(name))
print ('Nome com as letras maíusculas: {}'.format(name.upper()))
print ('Nome com as letras minusculas: {}'.format(name.lower()))
print ('Quantidade de caracteres no nome: {}'.format(len(name)))
print ('Quantas letras ao todo (sem considerar espaços): {}'.format(len(name) - name.count(' ')))
print ('Quantas letras tem o primeiro nome: {}'.format(name.find(' ')))
