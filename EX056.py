#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
homemmaisvelho = int(0)
nomemaisvelhor = str('')
somaidade = int(0)
s = int(0)
for c in range (1, 5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}º pessoa ([M] para homem e [F] para mulher): '.format(c)))
    somaidade = somaidade + idade
    if sexo == 'M' and homemmaisvelho < idade:
        homemmaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        s = s + 1
    print (' ')
print ('Média da idade do grupo: {}'.format(somaidade / 4))
print ('Nome do homem mais velho: {}'.format(nomemaisvelho))
print ('Quantidade de mulheres com menos de 20 anos: {}'.format(s))



        