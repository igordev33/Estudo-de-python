#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import datetime
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.now().year
idade = ano_atual - nasc

if idade <= 9:
    print ('É um atleta MIRIM')
elif idade <= 14 :
    print ('É um atleta INFANTIL')
elif idade <= 19 :
    print ('É um atleta JÚNIOR')
elif idade <= 25 :
    print ('É um atleta SÊNIOR')
else:
    print ('É um atleta MASTER')