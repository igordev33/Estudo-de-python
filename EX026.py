#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite alguma frase: ')).strip()
print ('A letra "A" aparece {} vezes na sua frase!'.format(frase.upper().count('A')))
print ('A letra "A" aparece pela primeira vez na posição {}'.format(frase.upper().find("A")+1))
print ('A letra "A" aparece pela ultima vez na posição {}'.format(frase.upper().rfind('A')+1))