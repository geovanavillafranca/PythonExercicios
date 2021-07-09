print('Fça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'
      'Ex: An Maria de Souza'
      'primeiro: Ana; último: Souza')
nome = str(input('Qual o seu nome completo?').strip())
novonome = nome.split()
print('O seu primeiro nome é {} e o segundo é {}.'
      .format(novonome[0], novonome[len(novonome)-1]))
