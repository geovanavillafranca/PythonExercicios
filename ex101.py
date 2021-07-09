print('Crie um programa que tenha uma função comando voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, '
    'retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.')


def voto(a):
    # o datetime so ira utilizar nessa função, fazendo esse import economiza MUITA memória
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA.'
    elif 18 > idade > 15 or idade >= 65:
        return 'VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO.'


# Programa Principal
print('-' * 40)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
