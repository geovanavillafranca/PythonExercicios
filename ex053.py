print('Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.'
      'Ex: Apos a sopa'
      'A sacada da casa'
      'A torre da derrota'
      'o lobo ama o bolo'
      'Anotaram a data da maratona')
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
            # len vai pegar o total de numero que contem na frase,
            # vai iniciar dando -1, finaliza até a ultima letra com -1 e o ultimo é para saber q é invertido
for letra in range(len(junto) -1, -1, -1):
      #variavel para armazenar a frase que vai ficar invertida
      inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
      print('Temos um palíndromo.')
else:
      print('A frase digitada não é um palíndromo.')
'''

## OU sem o for
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
      print('Temos um palíndromo.')
else:
      print('A frase digitada não é um palíndromo.')


