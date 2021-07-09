print('Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.')
dados = {}
jogadores = list()
tot = 0
gol = []
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    par = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, par):
        gol.append(int(input(f'     Quantos gols na partida {c}: ')))
    print('-=' * 30)
    dados['gols'] = gol[:]
    dados['total'] = sum(gol)
    gol.clear()
    jogadores.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print('-=' * 30)
# criando o cabecalho para a tabela
print(f'{"cod":>3}  ', end='')
# pega os valores da chave do dicionario
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
# tabela de jogadores
for i, v in enumerate(jogadores):
    # o valor para pegar o elemento
    print(f'{i:>3} ', end=' ')
    #para pegar as informacoes dentro de jogadores
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    esc = int(input('Mostrar os dados de qual jogador? [999 para parar] '))
    if esc == 999:
        break
    elif esc > len(jogadores)-1:
        print(f'ERRO! Não existe jogador com código {esc}.')
    elif esc <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[esc]["nome"]}:')
        for i, v in enumerate(jogadores[esc]['gols']):
            print(f'  => Na jogo {i}, fez {v} gols')
    print('-=' * 30)
print('<< VOLTE SEMPRE >>')
