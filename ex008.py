print('---- Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros ----')
m = float(input('Uma distância em metros: '))
cen = m * 100
mil = m * 1000
print('Sua altura convertido em centímetros fica {:.0f}cm e em milímetro fica {:.0f}mm' .format(cen, mil))
