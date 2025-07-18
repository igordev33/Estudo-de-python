#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                                C) O maior valor da segunda linha.

matriz = [[0 , 0 , 0] , [0 , 0 , 0] , [0 , 0 , 0]]
A = B = C = 0

for l in range (0 , 3):
    for c in range (0 , 3):
        matriz[l][c] = int(input(f'Digite o valor de [{l} , {c}]: '))
        if matriz[l][c] % 2 == 0:
            A += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            B += matriz[l][c]
        if matriz[l][c] == matriz[1][c]:
            if matriz[l][c] > C:
                C = matriz[l][c]
print('=-=' * 20)
for l in range (0 , 3):
    for c in range (0 , 3):
        print (f'[{matriz[l][c]:^5}]', end=' ')
    print('')

print ('=-=' * 20)
print (f'A) Valores pares somados: {A}')
print (f'B) A soma dos valores da terceira coluna: {B}')
print (f'C) O maior valor da segunda linha: {C}')