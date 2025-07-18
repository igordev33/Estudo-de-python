#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantida de tinta necessária para pintá-la, sabendo que cada litro de tinta pintura uma área de 2m**2.

wallheight = float(input('Digite a altura da parede: '))
wallwidth = float(input('Digite a larguda da parede: '))
wallm2 = wallheight * wallwidth

print('Para pintar uma parede de {} metros quadrados você irá precisar de {} latas de tinta'.format(wallm2, wallm2 / 2))