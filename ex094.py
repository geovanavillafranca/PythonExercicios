print('Crie um programa que leia nome, sexo, idade de várias pessoas, guardando os dados de cada uma pessoa em um dicionário e todos os dicionários em uma lista. '
      'No final, mostre: '
      'a - quantas pessoas foram cadastradas'
      'b - a média de idade do grupo'
      'c - uma lista com todas as mulheres'
      'd - uma lista com todas as pessoas com idade acima da média.')
c = 0
pessoa = list()
temp = dict()
somaf = 0
while True:
      # CADASTRO DAS PESSOAS #
      temp.clear()
      temp['nome'] = str(input('Nome: '))
      sexo = str(input('Sexo: [F/M] ')).lower().strip()[0]
      while sexo not in 'fm':
            print('ERRO! Por favor, digite apenas F ou M. ', end='')
            sexo = str(input('Sexo: [F/M] ')).lower().strip()[0]
      if sexo in 'fm':
            temp['sexo'] = sexo
      temp['idade'] = int(input('Idade: '))
      pessoa.append(temp.copy())
      c += 1
      resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      while resp not in 'sn':
            print('ERRO! Digite apensa S ou N. ', end='')
            resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
      if resp == 'n':
            break
print('-=' * 30)
# Quantas foram cadastradas
print(f'A) Foram cadastradas {c} pessoas.')
# média da idade
for i, v in enumerate(pessoa):
      somaf += v['idade']
med = somaf / c
print(f'B) A média da idade é de {med:.2f} anos.')
# mulheres cadastradas
print(f'C) A lista de mulheres cadastradas é ', end='')
for i, v in enumerate(pessoa):
      if v['sexo'] == 'f':
            print(v['nome'], end=' ')
# idade acima da média
print(f'\nD) A lista das pessoas com a idade acima da média é:')
for p in pessoa:
      if p['idade'] >= med:
            for k, v in p.items():
                  print(f'{k} = {v}; ', end='')
            print()
print('-=' * 30)
print('<< ENCERRADO >>')
