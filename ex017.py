'''from math import sqrt
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,'
      ' calcule e mostre o comprimento da hipotenusa.')
a = float(input('Digite o valor do cateto A:'))
b = float(input('Digite o valor do cateto B: '))
c = sqrt((a ** 2) + (b ** 2))
print('O valor da hipotenisa é {:.2f}.' .format(c))
'''
import math
a = float(input('Digite o valor do cateto A:'))
b = float(input('Digite o valor do cateto B: '))
c = math.hypot(a, b)
print('O valor da hipotenisa é {:.2f}.' .format(c))

