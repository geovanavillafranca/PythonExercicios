print('Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,'
      'já na posição correta de inserção (sem usar o sort()). No final,'
      'mostre a lista ordenanda na tela.')
lista = []
for c in range(0, 5):
      n = int(input('Digite um valor: '))
      # eu vou adicionar se ele for o primeiro ou entao se for o maior que o ultimo valor
      if c == 0 or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao final da lista..')
      else:
            pos = 0
            # ele vai da posicao 0 até a quantidade da lista
            while pos < len(lista):
                  # vai verificar dentro de cada posicao se o numero que ira inserir é menor ou igual a ele
                  if n <= lista[pos]:
                        lista.insert(pos, n)
                        print(f'Adicionado na posição {pos} da lista..')
                        break
                  pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem fora {lista}')
