#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e o nome do escolhido

import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

Alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(Alunos)
print('O aluno escolhido para apagar o quadro foi: {}'.format(sorteio))

