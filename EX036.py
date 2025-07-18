#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print ('                  Empréstimo TaKomKuNaVara')
print ('============================================================')
house_value = float(input('Primeiro digite o valor da casa que deseja comprar: '))
salary = float(input('Digite agora o seu salário: '))
payment_year = int(input('Agora me informe em quantos anos deseja a pagar a casa: '))
bill = house_value / (payment_year * 12)
print ('============================================================')

if salary * 0.3 > bill:
    print ('O seu empréstimo foi aprovado!')
    print ('Valor da parcela = {:.2f}'.format(bill))
    print ('Quantidade de parcelas: {}'.format(payment_year * 12))
else:
    print ('Infelizmente, o seu empréstimo foi reprovado! Tente um valor menor ou um número maior de parcelas.')
