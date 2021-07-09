print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os'
      'em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, '
      'serão exibidos todos os valores únicos digitados, em ordem crescente.')
lista = []
cont = 1
while True:
      num = int(input(f'Digite o {cont}° valor: '))
      cont += 1
      if num not in lista:
            print('Valor adicionado')
            lista += [num]
      else:
            print('Valor duplicado, não será adicionado.')
      escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      while escolha not in 'sn':
            escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      if escolha == 'n':
            print('-=-' *15)
            print('Finalizando programa...')
            print('-=-' *15)
            break
lista.sort()
print(f'Os valores em ordem crescente são {lista}')
