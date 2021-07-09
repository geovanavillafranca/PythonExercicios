print('Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:'
      'a - quantas vezes apareceu o valor 9'
      'b - em que posição foi digitado o primeiro valor 3'
      'c - quais foram os numeros pares')

n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))
print('--' * 20)
print(f'Você digitou {n}')
print('--' * 20)
print(f'O número 9 foi digitado {n.count(9)} vezes.')
# se tiver o número 3 no N, irá mostrar sua posição
if 3 in n:
      print(f'O número 3 está na {n.index(3)+1}ª posição.')
else:
      print('Você não digitou o número 3.')
print('Os números pares são: ', end='')
# em cada valor digitado, irá avaliar se é divisivel por 2 e irá descobrir se é par
for num in n:
      if num % 2 == 0:
            print(num, end=' ')


'''
num = (int(input('Digite um valor: ')),
      int(input('Digite um valor: ')),
      int(input('Digite um valor: ')),
      int(input('Digite um valor: ')))
print(f'Você digitou esses números: {num}')
print(f'O número nove foi digitado {num.count(9)} vezes')
if 3 in num:
      print(f'O número 3 está na  {num.index(3)+1}ª posição')
else:
      print('O número 3 não foi digitado.')
print(f'Os números pares são: ', end='')
for n in num:
      if n % 2 == 0:
            print(n, end=' ')
'''