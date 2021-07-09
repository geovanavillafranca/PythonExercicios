print('Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade '
      'da digitação de um número do tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.')

# Guanabara #
def leiaInt(msg):
      ok = False
      valor = 0
      while True:
            i = str(input(msg))
            try:
                  valor = int(i)
                  ok = True
            except:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            if ok:
                  break
      return valor


def leiaFloat(msg):
    while True:
        try:
            r = str(input(msg)).replace(',', '.')
            float(r)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return r


# Programa Principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {inteiro}')
print(f'Você acabou de digitar o número {real}')
