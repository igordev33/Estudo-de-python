#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Macaco', 'Leao', 'girafa', 'javali', 'porco', 'mamute', 'elefante', 'jacaré', 'crocodilo')
for palavra in tupla:
    print (f'\nNa palavra {palavra.upper()} temos as seguintes vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print (letra, end = ' ')