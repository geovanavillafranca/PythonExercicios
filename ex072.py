print('Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero'
      'até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')

#Tupla:
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        pos = int(input('Digite um número entre 0 a 20: '))
        #se estiver entre eles, irá para o proxima passo
        if pos >= 0 and pos <= 20:
            break
        print('Tente novamente. ', end='')
    # irá buscar no cont a posicao em que o usuario digitou, consequentemente, ira mostrar o número em relacao a posicao, 0, 1, 2, 3..
    print('Você digitou', cont[pos])
    # escolha se quer continuar
    escolha = str(input('Deseja continuar? [S/N] ')). lower().strip()[0]
    # caso o usuario não digitou s ou n, ira repetir ate digitar o correto
    while escolha not in 'sn':
        escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    # se for nao, o programa para
    if escolha == 'n':
        break

'''
while True:
      while True:
            n = int(input('Digite um número entre 0 a 20: '))
            if n >=0 and n <=20:
                  break
            print('Tente novamente. ', end='')
      # O número que o usuário digitou vai buscar na variavel que foi armazenada, então irá mostrar o número em extenso
      print(f'Você digitou {cont[n]}')

      # Escolher se quer continuar
      escolha = str(input('Você quer continuar? [S/N] ')).lower().strip()[0]
      while escolha not in 'sn':
            escolha = str(input('Você quer continuar? [S/N] ')).lower().strip()[0]
      if escolha == 'n':
            break
'''