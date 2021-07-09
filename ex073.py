print('Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, '
      'na ordem de colocação, Depois mostre: '
      'a - apenas os 5 primeiros colocadors.'
      'b - os últimos 4 colocados da tabela. '
      'c - uma lista com os times em ordem'
      'd - em que posição na tabela está o time da Chapecoense.')
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoence', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória','Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=-' * 40)
print(f'Os primeiros 5 colocados são: \n{times[:5]}')
print('=-' * 40)
print(f'Os últimos 4 colocados são: \n{times[-4:]}')
print('=-' * 40)
print(f'Em ordem alfabetica, os times são: \n{sorted(times)}')
print('=-' * 40)
print(f'O Chapecoense está na  {times.index("Chapecoence")+1}ª posição')


