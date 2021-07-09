from random import randint
print('Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, '
      'mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.')
comp = randint(0,10)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    res = jogador + comp
    while escolha not in 'pi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).lower().strip()[0]
    print('----' * 10)
    print(f'Você jogou {jogador} e o computador {comp}. Total deu {res}', end=' ')
    print('DEU PAR' if res % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'p':
        if res % 2 == 0:
            print('Você venceu! \nVamos jogar novamente...')
            vitoria += 1
        if res % 2 == 1:
            print('Você perdeu!')
            break
    if escolha == 'i':
        if res % 2 == 1:
            print('Você venceu! \nVamos jogar novamente...')
            vitoria += 1
        if res % 2 ==    0:
            print('Você perdeu!')
            break

print('----' *10)
print(f'GAME OVER. Você obteve {vitoria} vitórias.')


