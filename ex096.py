print('Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular'
      '(largura e comprimento) e mostre a área do terreno')
def area(lar, com):
      d = lar * com
      print(f'A área de um terreno {lar}x{com} é de {d:.2f}m².')


print('-' * 30)
print('--  CALCULADORA DE TERRENO  --')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
