print('---- Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e '
      'mostre quantos dólares ela pode comprar.---- \n Considera U$1.00 = 3.27 ')
num = float(input('Digite quanto você tem em dinheiro em sua carteira? R$ '))
dol = num / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}' .format(num, dol))
