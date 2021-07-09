print('Crie um programa que leia duas notas de um aluno e  calcule sua média, mostrando uma mensagem no final, '
      'de acordo com a média atingida:'
      'Média abaixo de 5.0: REPROVADO'
      'Média entre 5.0 a 6.9: RECUPERAÇÃO'
      'Média 7.0 ou superior: APROVADO')
print('---'*4 + ' CALCULADOR DE MÉDIA ' + '---'*4)
primeira = float(input('Qual foi sua primeira nota? '))
segunda = float(input('Qual foi a sua segunda nota? '))
media = (primeira + segunda) / 2
if media >= 7:
      print('Sua média é {}. Parabéns, você foi aprovado(a)!' .format(media))
elif media >= 5 and media <=6.9:
      print('Sua média é {}. Você está na recuperação!' .format(media))
else:
      print('Sua média é {}. Você foi reprovado(a)!' .format(media))

