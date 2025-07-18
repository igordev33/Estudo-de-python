#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior18 = homens = mulhermenor20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    if continuar == 'N':
        break
    print ('=-='*30)
print ('=-='*30)
print (f'{maior18} pessoas são maiores de 18 anos.')
print(f'{homens} pessoas são homens.')
print(f'{mulhermenor20} mulheres possuem menos de 20 anos.')