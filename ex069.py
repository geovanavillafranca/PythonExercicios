print('Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar'
      'se o usuário quer ou não continuar. No final, mostre:'
      'A - quantas pessoas tem mais de 18 anos.'
      'B - quantos homens foram cadastrados.'
      'C - quantas mulheres tem menos de 20 anos.')
maiorIdade = homens = menorMulher = 0
while True:
      idade = int(input('Digite sua idade:  '))
      sexo = ' '
      while sexo not in 'fm':
            sexo = str(input('Digite seu sexo [F/M] ')).lower().strip()[0]
      print('-----' *10)
      if idade >= 18:
            maiorIdade += 1
      if sexo == 'm':
            homens +=1
      else:
            if idade <= 20:
                  menorMulher +=1
      opcao = ' '
      while opcao not in 'sn':
            opcao = str(input('Quer continuar? [N/S] ')).lower().strip()[0]
      if opcao == 'n':
            break
      print('-----' *10)
print('Finalizando o programa..')
print(f'Tem {maiorIdade} pessoas maiores de 18 anos.')
print(f'Tem {homens} homens cadastrados.')
print(f'Tem {menorMulher} mulheres com menos de 20 anos.')
