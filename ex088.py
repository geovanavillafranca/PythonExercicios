print('Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntas quantos jogos serão '
      'gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.')
from time import sleep
from random import randint
lista = []
jogos = []
tot = 1
qnt = int(input('Quantos jogos você quer sortear? '))
while tot <= qnt:
      cont = 0
      # vai checar se vai ter numero repetido
      while True:
            num = randint(1, 60)
            if num not in lista:
                  lista.append(num)
                  cont += 1
            if cont >= 6:
                  break
      lista.sort()
      jogos.append(lista[:])
      lista.clear()
      tot += 1
print('-=' *3, f' SORTEANDO {qnt} JOGOS ', '-=' *3)
for p, v in enumerate(jogos):
      print(f'Jogo {p+1}: {v}')
      sleep(1)
