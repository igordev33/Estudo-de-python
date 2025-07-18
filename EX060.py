#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#A = int(input('Digite um número para calcular o seu fatorial: '))
#fatorial = A
#print ('{}! = {} x '.format(A, A), end = '')
#for c in range (A-1, 1, -1):
#    print (c, end=' x ')
#    fatorial = fatorial * c
#print (' 1 = {}'.format(fatorial))

A = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = A
while A > 1:
    print ('{} x '.format(A), end='')
    fatorial = fatorial * (A - 1)
    A -= 1
print ('1 = {}'.format(fatorial))