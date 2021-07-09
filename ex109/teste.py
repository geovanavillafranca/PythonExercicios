print('Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, '
      'informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108. ')
from ex109 import moeda
preco = float(input('Digite o preço: R$'))
taxa = 10
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando {taxa}%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo {taxa}%, temos R${moeda.diminuir(preco, taxa)}')
