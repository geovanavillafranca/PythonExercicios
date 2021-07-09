'''print('Crie um programa que leia vários números inteiros pelo teclado. '
      'O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. '
      'No final, mostre quantos números foram digitados e qual foi a soma entre eles '
      '(desconsiderando o flag)')
'''
'''
cont = 0
n1 = 0
sair = False
while not sair:
    n = int(input('Digite um valor [999 para parar]: '))
    cont +=1
    n1 += n
    if n == 999:
        n2 = n1 - 999
        cont -=1
        print('A soma entre todos os valores é {} e você digitou {} números.' .format(n2, cont))
        sair = True
print('FIM')
'''
######## GUANABARA #########
num = cont = soma = 0
num = int(input('Digite um valor [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor [999 para parar]: '))
print('A soma entre todos os valores é {} e você digitou {} números.'.format(soma, cont))



