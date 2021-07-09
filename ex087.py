print('Aprimore o desafio anterios, mostrando no final:'
      'a - a soma de todos os valores pares digitados.'
      'b - a soma dos valores da terceira coluna.'
      'c - o maior valor da segunda linha.')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = mai = col = 0

for linha in range(0, 3):
      for coluna in range(0, 3):
            matriz[linha][coluna] = int(input(f'Digite um valor [{linha}],[{coluna}]: '))
print('-=' * 20)
for linha in range(0, 3):
      for coluna in range(0, 3):
            print(f'[{matriz[linha][coluna]:^5}]', end='')
            if matriz[linha][coluna] % 2 == 0:
                  par += matriz[linha][coluna]
      print()

print(f'O valor total da somatoria dos pares é {par}')
for linha in range(0, 3):
      col += matriz[linha][2]
print(f'O valor da soma da terceira coluna é {col}')
for c in range(0, 3):
      if c == 0:
            mai = matriz[1][coluna]
      elif matriz[1][coluna]:
            mai = matriz[1][coluna]
print(f'O maior valor da segunda linha é {mai}')
