print('Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for'
      'diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule'
      'e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'
      '35 anos de contribuição')
from datetime import datetime
anoat = datetime.now().year
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
pessoa['idade'] = anoat - nasc
if pessoa['ctps'] != 0:
      pessoa['contratacao'] = int(input('Ano de contratação: '))
      pessoa['salario'] = float(input('Salário: R$'))
      pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - anoat)
print('-=' * 20)
for k, v in pessoa.items():
      print(f' - {k} tem o valor {v}')
