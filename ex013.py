print('---- Fça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. ----')
sal = float(input('Qual é o seu salário atual? '))
desc = (sal * 15) / 100
# novo = sal + (sal * 15 / 100)      vai fazer o desconto e somar o novo salario 
salAt = sal + desc
print('O seu salario teve aumento de {} então agora você recebe {}.' .format(desc, salAt))