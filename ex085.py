'''print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha '
      'separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente')
par = []
impar = []
total = []
for c in range(1, 8):
      n = int(input(f'Digite o {c}° valor: '))
      if n % 2 == 0:
            par.append(n)
      else:
            impar.append(n)
total.append(par)
total.append(impar)
print(f'Par: {sorted(total[0])} '
      f'\nImpar: {sorted(total[1])}')
print(total)
'''
##### SOLUÇÃO DO GUANABARA #####

num = [[],[]]
valor  = 0
for c in range (1, 8):
      valor = int(input(f'Digite o {c}° valor: '))
      if valor % 2 == 0:
            num[0].append(valor)
      else:
            num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Par {num[0]}')
print(f'Ímpar {num[1]}')

