#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
from time import sleep
choice = int(0)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
resultado = 0
while choice != 5:
    print ('     [1] Somar')
    print ('     [2] Multiplicar')
    print ('     [3] Maior')
    print ('     [4] Novos números')
    print ('     [5] Sair do programa')
    choice = int(input('>>>>>> Sua escolha: '))
    if choice == 1:
        resultado = n1 + n2
        print ('A soma entre {} + {} = {}'.format(n1, n2, resultado))
    elif choice == 2:
        resultado = n1 * n2
        print ('A multiplicação entre {} x {} = {}'.format(n1, n2, resultado))
    elif choice == 3:
        resultado = [n1, n2]
        maior = max(resultado)
        print ('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif choice == 4:
        print ('Informe os números novamente: ')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif choice == 5:
        print ('Saindo do programa . . . ')
    else:
        print ('>>>>Opção Inválida! Tente Novamente<<<<')
    sleep (3)
    print ('=-==-==-==-==-==-==-==-==-==-=')
print ('>>>>Programa Encerrado<<<<')