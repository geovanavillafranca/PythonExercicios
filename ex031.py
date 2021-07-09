print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,'
      ' cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
dist = float(input('Qual foi a distância percorrida? '))
if dist <= 200:
      print('O valor da viagem deu {:.2f} reais. ' .format( dist * 0.50 ))
else:
      print('O valor da viagem deu {:.2f} reais. ' .format( dist * 0.45 ))
