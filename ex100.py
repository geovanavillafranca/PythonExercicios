print('Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). '
      'A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai '
      'mostrar a soma entre todos os valores PARES sorteados pela função anterior.')
from random import randint
numero = []
def sorteia(lista):
      print(f'Sorteando 5 valores da lista: ', end='')
      for c in range(0, 5):
            n = randint(1, 10)
            lista.append(n)
            print(f'{n}', end=' ')
      print('PRONTO!')


def somaPar(lista):
      par = 0
      for c in lista:
            if c % 2 == 0:
                  par += c
      print(f'Somando os valores pares de {lista}, temos {par}')


sorteia(numero)
somaPar(numero)
