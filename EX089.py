##Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('=-=' *10)
print(f'{'Escola Takuna Vara':^30}')
print('=-=' * 10)
student_number = 0
student = []
student_list = []
while True:
    nome = str(input(f'Digite o nome do {student_number + 1}º aluno: ')).title()
    student.append(nome)
    n1 = float(input(f'Digite o valor da primeira nota de {nome}: '))
    student.append(n1)
    n2 = float(input(f'Digite o valor da segunda nota de {nome}: '))
    student.append(n2)
    media = (n1 + n2) / 2
    student.append(media)
    student_number += 1
    student_list.append(student[:])
    student.clear()
    choice = str(input('Deseja continuar [S/N]: ')).upper()
    print ('=-=' * 10)
    if choice in 'Nn':
        break
print (f'{'No.':^2}', f'{'Nome':<20}', f'{'Nota':^4}')
print ('-'*30)
for c in range (0, student_number):
    print (f'{c:^2}', f'{student_list[c][0]:<20}', f'{student_list[c][3]:^4}')
print ('=-='*10)
while True:
    student_choice = int(input('Digite o No. do aluno que deseja saber as notas (999 para sair): '))
    if student_choice == 999:
        print ('FINALIZANDO...')
        print ('<<< VOLTE SEMPRE >>>')
        break
    else:
        print(f'As notas de {student_list[student_choice][0]} são {student_list[student_choice][1]} e {student_list[student_choice][2]}.')

    