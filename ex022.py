print('Crie um programa que leia o nome completo de uma pessoa e mostre:'
      '\n 1- O nome com todas as letras maiúsculas. '
      '\n 2- O nome com todas minúsculas.'
      '\n 3- Quantas letras ao todo(sem os espaços)'
      '\n 4- Quantas letras tem o primeiro nome.')
nome = str(input('Digite seu nome completo: ')).strip()
print('1- {}' .format(nome.upper()))
print('2- {}' .format(nome.lower()))
nomediv = nome.split()
print('3- {}' .format(len(nome) - nome.count(' ')))
print('4- O seu primeiro nome tem {} letras' .format(len(nomediv[0])))
