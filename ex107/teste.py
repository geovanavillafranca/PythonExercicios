print('Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro e metade()'
      'Faça também um programa que importe esse módulo e use algumas dessas funções. ')
from ex107 import moeda
preco = float(input('Digite o preço: R$'))
taxa = 10
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando {taxa}%, temos R${moeda.aumentar(preco, taxa)}')
print(f'Diminuindo {taxa}%, temos R${moeda.diminuir(preco, taxa)}')
