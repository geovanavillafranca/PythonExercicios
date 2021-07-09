print('Faça um programa que leia nome e peso de várias pessoas, quardando tudo em uma lista.'
      'No final, mostre:'
      'a - quantas pessoas foram cadastrados.'
      'b - uma listagem com as pessoas mais pesadas.'
      'c - uma listagem com as pessoas mais leves')
dados = []
pessoas = []
mai = menor = 0
while True:
      print('--' * 15)
      # dados são as informacoes temporarias, para criar uma lista dentro de outra
      dados.append(str(input('Nome: ')))
      dados.append(float(input('Peso: ')))
      # se dados tiver 1 elemenorto, ira adicionar o peso:
      if len(pessoas) == 0:
            # vao receber o mesmo peso, pois nao tem menoror nem maior AINDA
            mai = menor = dados[1]
      else:
            # se o peso novo for maior que o anterior, ira receber o novo peso
            if dados[1] > mai:
                  mai = dados[1]
            # se o peso novo for menoror que o anterior, irá receber o novo peso
            if dados[1] < menor:
                  menor = dados[1]
      # pessoas é a lista principal, entao recebe uma copia de dados
      pessoas.append(dados[:])
      # dados é limpa para receber o proximo dado
      dados.clear()
      resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      while resp not in 'sn':
            resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      if resp == 'n':
            break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}Kg, peso de', end=' ')
for val in pessoas:
      if val[1] == mai:
           print(f'[{val[0]}]', end=' ')
print()
print(f'O menoror peso foi {menor}Kg, peso de', end=' ')
for val in pessoas:
      if val[1] == menor:
            print(f'[{val[0]}]', end=' ')
