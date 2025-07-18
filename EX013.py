#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

EmployeeName = str(input('Digite o nome do seu funcionário: '))
salary = float(input('Digite agora o salário atual desse funcionário: '))

print('Funcionário: {}'.format(EmployeeName))
print('Salário atual: {}'.format(salary))
print('Aumento: {}'.format(salary * 0.15))
print('Salário após o reajuste: R${}'.format(salary + (salary * 0.15)))