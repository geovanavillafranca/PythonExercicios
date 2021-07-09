import random
####### Meu #######
'''
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
num = int(input('Digite o seu palpite: '))
comp = random.randint(0,10)
contador = 0
while num != comp:
    contador += 1
    num = int(input('Você errou, tente de novo: '))
print('O número sorteado foi \033[35m{}\033[m' .format(comp))
print('Parabéns, você acertou! E você acertou com \033[1;33m{}\033[m tentativas.' .format(contador))
'''


########### GUANABARA ################
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
comp = random.randint(0,10)
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais... Tente mais uma vez.')
        elif jogador > comp:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!' .format(palpites))
