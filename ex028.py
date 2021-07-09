import random
from time import sleep
print('Escreva um programa que faça o computador pensar em um número inteiro entre 0 a 5 '
      'e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.'
      'Mostrar se venceu ou perdeu.')
num = int(input('Em qual número estou pensando? (0 a 5) '))
x = random.randint(0,5)
print('PROCESSANDO...')
sleep(1)
print('O número sorteado foi {}.' .format(x))
if num == x:
      print(' Você ACERTOU!!')
else:
      print('Você ERROU!!')
