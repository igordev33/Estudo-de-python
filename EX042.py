#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

A = float(input('Digite o comprimento da primeira reta: '))
B = float(input('Digite o comprimento da segunda reta: '))
C = float(input('Digite o comprimento da terceira reta: '))

if A + B > C and B + C > A and A + C > B:
    print ('Pode formar um triângulo!')
    if A == B and A == C:
        print ('E esse triangulo é EQUILÁTERO')
    elif A == B and A != C or A == C and A != B or B == C and B != A:
        print ('E esse triângulo é ISÓSCELES')
    elif A != B and A != C and B != C:
        print ('E esse triângulo é ESCALENO')
else:
    print ('Não pode formar um triângulo!')