print('Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos,'
      'na sequncia. No final mostre uma listagem de precos, organizando os dados em forma tabular.')
tupla = ('Banana', 2, 'Maça', 1, 'Arroz', 10,
         'Batata frita', 23, 'Chocolate', 5.36, 'Ovo', 9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
# primeiro saber quantos valores tem dentro da tupla, ai ira armazenar a posicao(0, 1, 2) dentro da variavel posição:
for posicao in range(0, len(tupla)):
    # se a posição for 'par' irá mostrar o nome dos produtos
    if posicao % 2 == 0:
        # o print da tupla na posição 'par' ex: tupla[0]
        print(f'{tupla[posicao]:.<30}', end='')
    else:
        # print na posição ímpar:
        print(f'R${tupla[posicao]:>6.2f}')

'''
for posicao in range(0, len(tupla)):
    if posicao % 2 == 0:
        print(f'{tupla[posicao]:.<30}', end='')
    else:
        print(f'R${tupla[posicao]:6.2f}')
'''