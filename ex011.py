print('---- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para'
      ' pintá-la,sabendo que cada litro de tinta, pinta uma área de 2m². ----')
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tin = area / 2
print('Você tem {:.2f}m² de área e precisa de {:.2f}l de tinta para pintar essa parede.' .format(area, tin))
