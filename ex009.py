from prettytable import PrettyTable
print('---- Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada. ----')
num = int(input('Digite um número: '))
n1 = num * 1
n2 = num * 2
n3 = num * 3
n4 = num * 4
n5 = num * 5
n6 = num * 6
n7 = num * 7
n8 = num * 8
n9 = num * 9
n10 = num * 10

# Cria a tabela
x = PrettyTable(['Multiplicação', 'Valores'])

# Alinha as colunas
x.align["Multiplicação"] = "l"
x.align["Valores"] = "r"

# Deixa um espaço entre a borda das colunas e o conteúdo (default)
x.padding_width = 1

# Adicionando linha por linha
x.add_row(['{} x 1 ='.format(num), n1])
x.add_row(['{} x 2 ='.format(num), n2])
x.add_row(['{} x 3 ='.format(num), n3])
x.add_row(['{} x 4 ='.format(num), n4])
x.add_row(['{} x 5 ='.format(num), n5])
x.add_row(['{} x 6 ='.format(num), n6])
x.add_row(['{} x 7 ='.format(num), n7])
x.add_row(['{} x 8 ='.format(num), n8])
x.add_row(['{} x 9 ='.format(num), n9])
x.add_row(['{} x 10 ='.format(num), n10])
print('Os valores são:\n', x)
