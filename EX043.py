#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print ('Vamos calcular o seu IMC')
peso = float(input('Digite primeiro a sua massa corporal: '))
altura = float(input('Digite agora a sua altura: '))
imc = peso / altura ** 2

print ('Peso = {:.2f}'.format(peso))
print ('Altura = {:.2f}'.format(altura))
print ('IMC = {:.2f}'.format(imc))

if imc <= 18.5:
    print ('Você está ABAIXO DO PESO.')
elif imc <=25:
    print ('Você está no seu PESO IDEAL.')
elif imc <=30:
    print ('Você está com SOBREPESO')
elif imc <=40:
    print ('Você está OBESO.')
elif imc > 40:
    print ('Você está com OBESIDADE MÓRBIDA')
