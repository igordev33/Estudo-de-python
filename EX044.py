#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

price = float(input('Digite aqui o valor do seu produto: R$'))
print ('Agora digite a condição de pagamento: ')
print ('[1] para à vista no dinheiro ou cheque')
print ('[2] para pagamentos à vista no cartão')
print ('[3] para pagamentos em até 2x no cartão')
print ('[4] para pagamento em 3x ou mais no cartão')
payment_choice = int(input('Sua escolha: '))

if payment_choice == 1:
    print ('Parabéns! Você ganhou 10% de desconto')
    print ('Valor total da compra: R${:.2f}'.format(price - (price * 0.1)))
elif payment_choice == 2:
    print ('Parabéns! Você ganhou 5% de desconto')
    print ('Valor total da compra: {:.2f}R$'.format(price - (price * 0.05)))
elif payment_choice == 3:
    print ('Valor total da compra: {:.2f}R$'.format(price))
    print ('Total de parcelas: 2')
    print ('Valor das parcelas: {:.2f}R$'.format(price / 2))
elif payment_choice == 4:
    parcel_number = int(input('Digite em quantas parcelas deseja pagar: '))
    if parcel_number >= 3:
        print ('Valor total da compra: {:.2f}R$'.format(price + price * 0.2))
        print ('Quantidade de parcelas: {}'.format(parcel_number))
        print ('Valor das parcelas: {:.2f}R$'.format((price + price * 0.2) / parcel_number))
    else:
        print ('Valor de parcelas menor do que o esperado, escolha outra opção e evite pagar juros.')
else:
    print ('OPÇÃO INVÁLIDA!')
