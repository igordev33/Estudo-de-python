#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: -O primeiro valor é maior  -O segundo valor é maior  -Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print ('Primeiro valor: {}'.format(n1))
print ('Segundo valor: {}'.format(n2))

if n1 > n2 :
    print ('O primero valor é maior')
elif n2 > n1 :
    print ('O segundo valor é maior')
else:
    print ('Não existe valor maior, os dois são iguais')
    

