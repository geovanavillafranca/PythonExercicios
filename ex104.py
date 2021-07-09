print('Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,'
      'só que fazendo a validação para aceitar apenas um valor numérico.'
      'Ex: n = leiaInt("Digite um número")')


def leiaInt(msg):
      #criar uma nova variavel, que assim faz com q a função seja convertida para String
      num = str(input(msg))
      while not num.isnumeric():
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            num = input('Digite um número: ')
      if num.isnumeric():
            return num



'''
# Guanabara #
def leiaInt(msg):
      ok = False
      valor = 0
      while True:
            n = str(input(msg))
            if n.isnumeric():
                  valor = int(n)
                  ok = True
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            if ok:
                  break
      return valor

'''
# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
