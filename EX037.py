#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print ('Selecione um dos números a seguir para converter seu número: ')
print ('[1] para converter em binário.')
print ('[2] para converter em octal.')
print ('[3] para converter em hexadecimal.')
choice = int(input('Digite aqui a sua escolha: '))

if choice == 1:
    print ('Binário = {}'.format(bin(num)))
elif choice == 2:
    print ('Octal = {}'.format(oct(num)))
elif choice == 3:
    print ('Hexadecimal = {}'.format(hex(num)))
else:
    print ('OPÇÃO INVÁLIDA!!!')