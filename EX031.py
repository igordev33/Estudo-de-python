#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print ('Companhia De Transporte TaComKuNaVara')
print ('--------------------------------------')
km = float(input('Digite aqui a distância da sua viagem em Km: '))
print ('--------------------------------------')
if km <= 200:
    ticket = float(0.5 * km)
    print ('Valor da passagem: {:.2f}R$'.format(ticket))
else:
    ticket = float(0.45 * km)
    print ('Valor da passagem: {:.2f}R$'.format(ticket)) 
print ('--------------------------------------')  
print ('A companhia TaComKuNaVara agradeçe a preferência e deseja uma ótima viagem.') 