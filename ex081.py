print('Crie um programa que vai ler vários números e colocar em uma lista.'
      'Depois disso, mostre:'
      'a - quantos números foram digitados.'
      'b - a lista de valores, ordenada de forma decrescente.'
      'c - se o valor 5 foi digitado e está ou não na lista.')
n = []
while True:
      n.append(int(input('Digite um valor: ')))
      escolha = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
      while escolha not in 'sn':
            escolha = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
      if escolha == 'n':
            print('-=' * 20)
            print(f'Finalizando o programa...')
            break
print('-=' *20)
print(f'você digitou {len(n)} elementos.')
n.sort(reverse=True)
print(f'Sua ordem descrescente é {n}')
if n.count(5):
      print('O número 5 faz parte da lista.')
else:
      print('O número 5 está fora da lista.')
