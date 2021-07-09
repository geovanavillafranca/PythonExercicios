from datetime import date
print('Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:'
      'Se ele ainda vai se alistar ao serviço militar.'
      'Se está na hora de se alistar.'
      'Se já passou do tempo do alistamento.'
      'Seu programa também deverá mostrar o tempo que falta ou que passou do prazo ')

ano = int(input('Qual seu ano de nascimento? '))
anoat = date.today().year
idade = anoat - ano
sexo = str(input('Digite F para feminino e M para masculino: ')).lower()
if sexo == 'm':
      if idade < 18:
            print('Você ainda vai se alistar ao serviço militar.')
            temp = 18 - idade
            print('Falta {} anos para você se alistar.' .format(temp))
            anoali = anoat + temp
            print('Seu alistamento será em {}' .format(anoali))
      elif idade == 18:
            print('Você tem que se alistar IMEDIATAMENTE')
      else:
            print('Seu tempo de alistamento já passou.')
            temp = idade - 18
            print('Faz {} anos que você se alistou.' .format(temp))
            anoali = anoat - temp
            print('Seu alistamento foi em {}.' .format(anoali))
else:
      print('Você não precisa se alistar')