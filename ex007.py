print('---- Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média ----')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é: {:.1f}' .format(media))
if media >= 6:
    print('Você foi APROVADO')
else:
    print('Você foi REPROVADO')
