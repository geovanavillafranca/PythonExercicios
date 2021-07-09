print('Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre'
      'A - qual é o total gasto na compra'
      'B - quantos produtos custam mais de R$1000'
      'C - qual é o nome do produto mais barato.')
total = maisMil = menor = cont = 0
barato = ''
while True:
      nome = str(input('Nome do produto: '))
      preco = int(input('Preço: R$ '))
      cont += 1
      print('-----' *10)
      total += preco
      if preco > 1000:
            maisMil += 1
      if cont == 1 or preco < menor:
            menor = preco
            barato = nome
      resp = ' '
      while resp not in 'sn':
            resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      print('-----' * 10)
      if resp == 'n':
            break
print(f'O total da compra foi R${total:.2f}')
print(f'Teve {maisMil} produtos que custaram mais que R$1000.')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
