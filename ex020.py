import random
print('O mesmo professor do desafio anterios quer soetear a ordem de aprentação de'
      'trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
a = input('Digite o nome do 1° grupo: ')
b = input('Digite o nome do 2° grupo: ')
c = input('Digite o nome do 3° grupo: ')
d = input('Digite o nome do 4° grupo: ')
nomes = [a, b, c, d]
random.shuffle(nomes)
print('A ordem de aprentação será: ')
print(nomes)
