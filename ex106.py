print('Faça um mini-sistema que utilize o interactive Help do Python. O ussuário vai digitar o comando e o manual vai aparecer. '
      'Quando o usuário digitar a palavra "FIM", o programa se encerrará. OBS: use cores')
from time import sleep

'''
def sis(s):
    print('\033[0;30;42m~' * len(s))
    print(f'{s}')
    print(len(s) * '~')


def decisao():
    while True:
        sis('  SISTEMA DE AJUDA PyHELP  ')
        esc = str(input('\033[mFunção ou Biblioteca > ')).lower()
        if esc == 'fim':
            fim = '  ATÉ LOGO!  '
            print('\033[30;41m~' * len(fim))
            print(fim)
            print('~' * len(fim))
            print('\033[m')
            break
        pyhelp(esc, f'  Acessando o manual do comando {esc}  ')

def pyhelp(x, ac):
    print('\033[0;30;44m~' * len(ac))
    print(ac)
    print('~' * len(ac))
    print('\033[m')
    sleep(1.2)
    print('\033[7m')
    print(f'{help(x)}\033[m')


decisao()
'''
# Guanabara #

# tupla com uma 'lista' de cores Global, pois está fora da função
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7m'       # 6 - branco
    );

# Rebece o comando em que quer executar
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


# Função em que personaliza o titulo
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)





