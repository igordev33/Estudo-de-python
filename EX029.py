#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

car_speed = int(input('Digite a velocidade do carro: '))
if car_speed > 80:
    print ('Você foi multado!')
    print ('O valor da multa é {}R$'.format((car_speed - 80) * 7))
else: 
    print ('Dentro do limite de velocidade')