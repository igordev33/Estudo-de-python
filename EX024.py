#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#frase.find() #Mostra localização inicial de alguma palavra inserida em ()

name = str(input('Digite o nome da cidade: ').strip())
print (name[:5].upper() == "SANTO")