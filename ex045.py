from random import randint
from time import sleep
print('Crie um programa que faça o computador jogar Jokenpô com você')
print('===' *5 + ' VAMOS JOGAR JOKENPÔ ' + '===' *5)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {} ' .format(itens[computador]))
print('Jogador jogou {} ' .format(itens[jogador]))
print('-=' * 11)
if computador == 0: # comptador jogou pedra
    if jogador == 0:
            print('EMPATE')
    elif jogador == 1:
            print('JOGADOR VENCE')
    elif jogador == 2:
            print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # comptador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # comptador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')