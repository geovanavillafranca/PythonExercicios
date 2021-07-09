from datetime import date
print('A confederação nacional de natação precisa de um programa que leia o ano '
      'de nascimento de um atleta e mostre sua categoria, de acordo com a idade:'
      'Até 9 anos: MIRIM'
      'Até 12 anos: INFANTIL'
      'Até 19 anos: JUNIOR'
      'Até 20 anos: SÊNIOR'
      'Acima: MASTER')
ano = int(input('Em qual ano você nasceu? '))
anoat = date.today().year
idade = anoat - ano
print('----' *6)
print('Sua idade é {} anos.' .format(idade))
if idade <= 9:
      print('Sua categoria é MIRIM')
elif idade <= 12:
      print('Sua categoria é INFANTIL')
elif idade <= 19:
      print('Sua categoria é JUNIOR')
elif idade <= 25:
      print('Sua categoria é SÊNIOR')
else:
      print('Sua categoria é MASTER')