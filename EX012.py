#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

productname = str(input('Digite o nome do produto: '))
productvalue = float(input('Digite o valor do produto: '))

print('Nome do produto: {}'.format(productname))
print('Valor do produto: R${}'.format(productvalue))
print('Valor do desconto: R${}'.format(productvalue * 0.05))
print('Valor do produto com desconto de 5%: R${}'.format(productvalue - (productvalue * 0.05)))