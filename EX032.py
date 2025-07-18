#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#1 - Verifique se os dois últimos algarismos do ano são múltiplos de 4. Por exemplo, 2024 é bissexto porque 24 é múltiplo de 4. 
#2 - Se o ano for centenário, verifique se é divisível por 400. Por exemplo, 2000 foi bissexto porque foi divisível por 400. 

year = int(input('Para saber se um ano é bissexto, digite a seguir o ano: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: 
    print ('O ano de {} é BISSEXTO!'.format(year))
else:
    print ("O ano de {}, NÃO é bissexto".format(year))


