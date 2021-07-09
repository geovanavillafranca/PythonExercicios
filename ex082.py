print('Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter'
      ' apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.')
par = []
impar = []
lista = []
while True:
      lista.append(int(input('Digite um valor: ')))
      escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      while escolha not in 'sn':
            escolha = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      if escolha == 'n':
            break
for pos, val in enumerate(lista):
      if val % 2 == 0:
            par.append(val)
      else:
            impar.append(val)
print(f'A lista completa é {lista}')
print(f'A lista com os pares é {par}')
print(f'A lista com os ímpares é {impar}')
