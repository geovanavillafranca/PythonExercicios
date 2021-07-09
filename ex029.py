print('Escreva um programa que leia a velocidade de uma carro. Se ele ultrapassar 80km.'
      ' mostre uma mensagem dizendo que ele foi multado.'
      'A multa vai custar R$7.00 por cada km acima do limite.')
velocidade = float(input('Qual foi a velocidade percorrida? '))
if velocidade > 80:
      print('Você ultrapassou o limite de velocidade que é 80Km/h, então sua multa é de {:.2f} reais.' .format((velocidade-80) * 7))
print('Tenha um bom dia! Dirija com segurança!')
