print('Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,'
      'mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.')
'''
dados = []
alunos = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('1° Nota: ')))
    dados.append(float(input('2° Nota : ')))
    dados.append((dados[1] + dados[2]) / 2)
    alunos.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print('--' * 15)
print(f'{"ID":<0} {"NOME":^20} {"MÉDIA":>0} ')
print('--' * 15)
for pos, val in enumerate(alunos):
    print(f'{pos:<1}  {val[0]:^20}{val[3]:>5} ')
cada = int(input('Digite o ID do aluno para ver a nota individual ou 999 para parar: '))
while cada != 999:
    print(f'Notas de {alunos[cada][0]} são: [{alunos[cada][1]}, {alunos[cada][2]}]')
    cada = int(input('Digite o ID do aluno para ver a nota individual ou 999 para parar: '))
print('Volte sempre!')'''

##### GUANABARA #####

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 20)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notar de {ficha[opc][0]} são: {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
