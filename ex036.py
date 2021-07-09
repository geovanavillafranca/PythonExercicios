print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. '
      'Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. '
      'A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')
print('-----' *4 + ' EMPRÉSTIMO ' + '-----' *4)
casa = float(input('Qual é o valor da casa em que você quer comprar R$'))
salario = float(input('Quant é o seu sálario R$'))
anos = int(input('Em quantos anos você quer pagar? '))
salmax = (salario * 30) / 100
prest = casa / (anos * 12)
print('Para pagar a casa de R${} em {} anos a prestação será de R${:.2f}.' .format(casa, anos, prest))
if prest >= salmax:
      print('O seu empréstimo foi NEGADO!')
else:
      print('O seu empréstimo foi CONCEDIDO!')
