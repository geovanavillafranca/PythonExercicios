print('Escreva um programa que pergunte a qunatidade de km percorridos por um carro alugado e '
      'a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o'
      'carro custa R$60 por dia e R$0,15 por Km rodado.')
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Kms rodados? '))
pagar = (60 * dia) + (0.15 * km)
print('Você tera que pagar é R${:.2f}.' .format(pagar))
