#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite o número do qual deseja saber a sua tabuada: '))

for c in range (1, 11):
    print ('{} x {} = {}'.format(tabuada, c, c * tabuada))