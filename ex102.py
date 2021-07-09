print('Crie um programa que tenha uma função fatorial() que receba dois parâmetross: o primeiro que indique o '
      'número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado '
      'ou não na tela o processo de cálculo do fatorial.')


def fatorial(n=0, show=False):
      """
      -> Calcula o Fatorial de um número.
      :param n: O número a ser calculado.
      :param show: (opcional) Mostra ou não a conta.
      :return: O valor do Fatorial de um número n.
      """
      fat = 1
      for c in range(n, 0, -1):
            fat *= c
            if show == True:
                  print(c, end='')
                  if c > 1:
                        print(' x ', end='')
                  else:
                        print(' = ', end='')
      return fat


# Programa Princiapal
print(fatorial(5, show=True))
#help(fatorial)
