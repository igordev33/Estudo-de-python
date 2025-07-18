#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print ('Vamos fazer uma bricadeira !! Me diga um número, e te direi se é par ou impar !')
number = int(input("Vamos lá ! Me diz ai o seu número: "))
print ('Seu número é: {}'.format(number))
if number % 2 == 0:
    print ('Seu número é par !!!')
else:  
    print ('Seu número é impar !!!')
    
