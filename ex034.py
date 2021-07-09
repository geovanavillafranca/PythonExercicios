print('Escreva um programa que pergunte o salário de um funcionário e calcule o calor do seu aumento.'
      'Para salários superiores a R$1.250,00, calcule um aumento de 10%'
      'Para inferiores ou iguais, o aumento é de 15%.')
salario = float(input('Qual é o seu salário? R$'))
if salario <= 1250:
      novo = salario + (salario* 15 / 100)
      print('Seu salário com aumento de 15% ficou RS{}' .format(novo))
else:
      novo = salario + (salario * 10 /100)
      print('Seu salário com aumento de 10% ficou RS{}' .format(novo))
