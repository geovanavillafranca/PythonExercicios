from datetime import date
print('Crie um programa que leia o ano de nascimento de sete pessoas.No final, mostre quantas pessoas ainda não atingiram'
      ' a maioridade e quantas já são maiores ')

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
      nascimento = int(input('Em que ano a {}° pessoa nasceu? ' .format(c)))
      idade = atual - nascimento
      if idade >= 18:
            totmaior += 1
      else:
            totmenor += 1
print('Tem {} maiores de idade.' .format(totmaior))
print('Tem {} menores de idade.' .format(totmenor))