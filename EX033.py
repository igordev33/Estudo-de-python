#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

N1 = int(input('Digite o valor de N1: '))
N2 = int(input('Digite o valor de N2: '))
N3 = int(input('Digite o valor de N3: '))

print ('N1: {}'.format(N1))
print ('N2: {}'.format(N2))
print ('N3: {}'.format(N3))

if N1 > N2 and N1 > N3:
    print ('O valor de N1 que é igual a {} é maior!'.format(N1))
elif N2 > N1 and N2 > N3:
    print ('O valor de N2 que é igual a {} é maior!'.format(N2))
elif N3 > N1 and N3 > N2: 
    print ('O valor de N3 que é igual a {} é maior!'.format(N3))


if N1 < N2 and N1 < N3:
    print ('O valor de N1 que é igual a {} é o menor valor!'.format(N1))
elif N2 < N1 and N2 < N3:
    print ('O valor de N2 que é igual a {} é o menor valor!'.format(N2))
elif N3 < N1 and N3 < N2:
    print ('O valor de N3 que é igual a {} é o menor valor!'.format(N3))
