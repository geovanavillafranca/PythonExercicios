'''
from math import trunc
print('Crie um programa que leia um númeiro Real qualquer pelo teclado e mostre na tela a sua porção inteira.')
num = float(input('Digite um número real:'))
print('O número {} e sua porçã inteira é {}.' .format(num, trunc(num)))
'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num,int(num)))