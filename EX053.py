#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).replace(' ','').upper()
inverso = ''
for palavra in range (len(frase)-1, -1, -1):
    inverso = inverso + frase[palavra]
print ('O inverso de {} é {}.'.format(frase, inverso))
if frase == inverso:
    print ('A frase é um palíndromo')
else:
    print ('A frase não é um palíndromo')
