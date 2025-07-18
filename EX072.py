#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Conjunto_de_numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero_escolhido = int(input('Digite um número entre 0 e 20 e te mostrarei ele por extenso: '))
while True:
    if numero_escolhido >= 0 and numero_escolhido <= 20:
        break
    else: 
        print ('Opção inválida, tente novamente.')
        numero_escolhido = int(input('Digite um número entre 0 e 20: '))
print (f'O número {numero_escolhido} escrito por extenso é {Conjunto_de_numeros[numero_escolhido]}')
