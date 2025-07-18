#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
print ('O primeiro nome do seu nome é {}'.format(nome[:nome.find(' ')]))
print ('O último nome do seu nome é {}'.format(nome[nome.rfind(' '):]))
