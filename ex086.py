'''print('Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.'
      'No final mostre a matriz na tela, com a formatação correta.')
mat = []
for c in range(1, 10):
    mat.append(int(input(f'Digite o {c}° valor da matriz: ')))
print('-=' * 15)
print(f'{"MATRIZ":^30}')
print('-=' * 15)
'''
#print(f'''
#[{mat[0]}][{mat[1]}][{mat[2]}]
#[{mat[3]}][{mat[4]}][{mat[5]}]
#[{mat[6]}][{mat[7]}][{mat[8]}]''')

# já começa vazia
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        # para trocar os valores ja existentes
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}],[{coluna}]:'))
print('-=' * 20)
#esses sao para mostrar na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
