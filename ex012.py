print('---- Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% desconto. ----')
prod = input('Qual é o produto? ')
preco = float(input('Digite o preço do produto: '))
desc = (preco * 5) / 100
# novo = preco - (preco * 5 / 100)          assim ja da o valor direto
precoAt = preco - desc
print('A(O) {} com desconto de 5% fica {:.2f}' .format(prod, precoAt))
