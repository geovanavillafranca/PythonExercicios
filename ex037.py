print('Escreva um programa que leia um número inteiro qualquer e peça para o usuário'
      'escolher qual será a base de conversão:'
      '1 para binário '
      '2 para octal'
      '3 para hexadecimal')
num = int(input('Digite um número inteiro: '))
escolha = int(input('\n[1] - binário \n[2] - octal \n[3] - hexadecimal \nEscolha um número para converter:'))
if escolha == 1:
     print(' {} convertido para BINÁRIO é igual a {}.' .format(num, bin(num)[2:]))
elif escolha == 2:
      print(' {} convertido para OCTAL é igual a {}.' .format(num, oct(num)[2:]))

elif escolha == 3:
      print(' {} convertido para HEXADECIMAL é igual a {}.' .format(num, hex(num)[2:]))
else:
      print('Opção inválida. Tente novamente')