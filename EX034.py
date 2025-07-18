#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

name = str(input('Digite o nome do seu funcionário que irá receber aumento: '))
salary = float(input('Digite agora o salário atual deste funcionário: '))

if salary >= 1250:
    salary = salary * 0.1 + salary
else:
    salary = salary * 0.15 + salary

print ('O sálario de {} após o aumento será de {}R$'.format(name , salary))