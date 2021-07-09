print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado '
      'e as suas respectivas posições na lista.')
num = []
for c in range(0,5):
      num.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou esses valores: {num} ')
maior = max(num)
menor = min(num)
print(f'O maior valor é {maior} e está na posição ', end='')
for pos, val in enumerate(num):
      if val == maior:
            print(f'{pos}.. ', end=' ')
print(f'\nO menor valor é {menor} e está na posição ', end='')
for pos, val in enumerate(num):
      if val == menor:
            print(f'{pos}.. ', end=' ')
