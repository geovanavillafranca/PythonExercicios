import random
print(' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. '
      'Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')
a = input('Digite o nome do 1° aluno: ')
b = input('Digite o nome do 2° aluno: ')
c = input('Digite o nome do 3° aluno: ')
d = input('Digite o nome do 4° aluno: ')
'''nomes = [a, b, c, d]
x = random.choice(nomes)
print('O aluno sorteado foi {}' .format(x))
'''
print('O aluno sorteado foi {}' .format(random.choice([a, b, c, d])))