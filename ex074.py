print('Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, '
      'mostre a listagem de números gerados e também indique o menor e o meior valor que estão na tupla.')
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior é {max(num)}')
print(f'O menor é {min(num)}')

