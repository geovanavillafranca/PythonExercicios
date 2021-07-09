print('Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:'
      '0 primeiro valor é maior'
      '0 segundo valor é maior '
      'Não existe valor maior, os dois são iguais')
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))

if primeiro > segundo:
      print('O primeiro valor é maior que o segundo.')
elif segundo > primeiro:
      print('O segundo valor é maior que o primeiro.')
else:
      print('Não exite valor maior, os dois são iguais.')
