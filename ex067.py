print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. '
      'O programa será interrompido quando o número solicitado for negativo. ')
print('--' *5, ' CALCULADORA DE TABUADA ',  '--' *5)
opcao = 's'
while True:
    num = int(input('Digite um número: '))
    print('-------' *5)
    if num < 0:
        break
    for c in range(1, 11):
        total = c * num
        print(f'{c} x {num} = {total}')
    print('-------' * 5)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')