#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

openpar = 0
closepar = 0
expr = str(input('Digite uma expressão matemática: '))
for simb in expr:
    if simb == '(':
        openpar += 1
    if simb == ')':
        closepar += 1
if openpar == closepar:
    print ('Sua expressão está correta.')
else:
    print ('Sua expressão está errada.')