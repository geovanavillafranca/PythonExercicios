print('Adapte o código do desafio 107, criando uma função adicional chamada moeda() eu consiga mostrar os valores como um '
      'valor monetário formatado.')
from ex108 import moeda
preco = float(input('Digite o preço: R$'))
taxa = 10
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é R${moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando {taxa}%, temos R${moeda.moeda(moeda.aumentar(preco, taxa))}')
#  print(f'Diminuindo {taxa}%, temos R${moeda.diminuir(preco, taxa)}')
