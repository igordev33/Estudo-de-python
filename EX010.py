print('-------------------------------------')
print('     AGÊNCIA DE TROCA PÉ NA COVA     ')
print('-------------------------------------')
real = float(input('Digite quanto de dinheiro você tem em R$: '))
dolar = real / 5.81
euro = real / 5.99
libra = real / 7.21
print('Com {}R$ você pode comprar {}U$, ou {}€, ou {}£'.format(real, dolar, euro, libra))

