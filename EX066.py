#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

S = C = 0 
while True:
    N = int(input('Digite um número: [999 para parar] '))
    if N == 999:
        break
    S += N
    C += 1
print (f'Ao todo foram digitados {C} números.')
print(f'A soma de todos os números digitados é {S}.')
