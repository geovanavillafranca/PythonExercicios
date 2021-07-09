print('Desenvolva um programa que leia o comprimento de três retas '
      'e diga ao usuário se elas podem ou não formar um triângulo.')
print('Analisador de triângulos')
print('----' *10)
r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
print('----' *10)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')