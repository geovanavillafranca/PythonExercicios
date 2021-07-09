print('Faça um programa que tenha uma função chamada escreva(), que receba'
      'um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'
      'Ex: escreva("Olá, Mundo!)'
      'Saída: ~~~~~~~'
      '      Olá, Mundo! '
      '       ~~~~~~~ ')
def escreva(st):
      print('~' * (len(st) + 4))
      print(f'  {st}')
      print('~' * (len(st) + 4))


escreva('Olá, Mundo!')
escreva('Curso em Vídeo')
escreva('Python é muito legal')
