#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print (f'Você digitou os números {num}')

if 9 in num:
    print (f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print (f'Não foi inserido o valor 9 dentro desta tupla.')

if 3 in num:
    print (f'O número 3 apareceu na posição {num.index(3) + 1}º') 
else:
    print ('O valor 3 não foi inserido dentro desta tupla.')

print ('Os seguintes número pares apareceram na tupla:', end = (' '))
for n in num:
    if n % 2 == 0:
        print (n, end = (' '))