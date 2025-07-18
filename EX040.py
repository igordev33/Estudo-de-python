#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nome = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
print ('Nome do aluno: {}'.format(nome))
print ('Primeira nota: {:.2f}'.format(n1))
print ('Segunda nota: {:.2f}'.format(n2))
print ('Média: {:.2f}'.format(m))

if m >= 7:
    print('{} está APROVADO'.format(nome))
elif m < 7 and m >= 5:
    print ('{} está de RECUPERAÇÃO'.format(nome))
else:
    print ('{} está REPORVADO'.format(nome))