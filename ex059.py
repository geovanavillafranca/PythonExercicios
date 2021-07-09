from time import sleep
print('Crie um programa que leia dois valores e mostre um menu na tela:'
      '[1] soma [2] multiplixar [3] maior [4] novos números [5] sair do programa'
      'Seu programa deverá realizar a operação solicitada em cada caso.')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:
      print('-------' * 5)
      opcao = int(input('''O que deseja fazer agora? 
      [1] somar
      [2] multiplicar 
      [3] maior
      [4] novos números
      [5] sair do programa
      Qual a sua escolha: '''))
      print('-------' * 5)
      if opcao == 1:
            res = num1 + num2
            print('A soma entre os valores {} + {} = {}' .format(num1, num2, res))
      elif opcao == 2:
            res2 = num1 * num2
            print('A multiplicação entre os valores {} x {} = {}' .format(num1, num2, res2))
      elif opcao == 3:
            if num1 > num2:
                  print('Entre {} e {} o número maior é {}' .format(num1, num2, num1))
            else:
                  print('Entre {} e {} o número maior é {}' .format(num1, num2,num2))
      elif opcao == 4:
            num1 = int(input('Digite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))
      elif opcao == 5:
            print('Finalizando...')
            sleep(2)
            print('Fim do programa! Volte sempre!')
            sair = True
      else:
            print('Opção inválida. Tente novamente.')
