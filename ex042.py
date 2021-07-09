print(''' Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
      Equilátero: todos os lados iguais
      Isósceles: dois lados iguais
      Escaleno: todos os lados diferentes''')
r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
print('----' *10)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM triângulo!')
    if r1 == r2 == r3:
          print('É um triângulo EQUILÁTERO')
    elif (r1 == r2 or r1 == r3 or r2 == r3):
          print('É um triângulo ISÓSCELES')
    elif r1 != r2 != r3 != r1:
          # r1 é diferente de r2 e r2 é diferente de r3 e r3 é diferente de r1
          print('É um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
