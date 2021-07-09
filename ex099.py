print('Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.'
      'Seu programa tem que analisasr todos os valores e dizer qual deles é o maior.')
from time import sleep

def maior(* l):
      maior = cont = 0
      print('-=' * 30)
      print(f'Analisando os valores passados...')
      for c in l:
            print(c, end=' ')
            sleep(0.5)
            if cont == 0:
                  maior = c
            else:
                  if maior < c:
                        maior = c
            cont += 1
      print(f'Foram informados {len(l)} valores ao todo.')
      print(f'O maior número cadastrado foi {maior}.')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
