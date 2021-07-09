print('Crie um programa que leia vários números inteiros pelo teclado. No final da'
      'execução, mostre a média entre todos os valores e qual foi o mair e o menor valores lidos.'
      'o programa deve perguntar ao usuário se ele quer ou não a digitar valores.')

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
      num = int(input('Digite um número: '))
      soma += num
      quant += 1
      if quant == 1:
            maior = menor = num
      else:
            if num > maior:
                  maior = num
            if num < menor:
                  menor = num
      resp = str(input('Quer continuar? [S/N] ' )).upper().strip()[0]
media = soma / quant
print(f'A soma entre todos os valores é {soma}.'
      f' \nA média dos valores é {media}.'
      f' \nVocê digitou {quant} números.'
      f' \nO maior número digitado foi {maior} e o menor foi {menor}.')


