def aumentar(p=0, t=0, formato=False):
    res = p + (p * t / 100)
    # se for falso, só mostrara o res sem formatado, sendo verdaderio, mostrara formatado
    return res if formato is False else moeda(res)


def diminuir(p=0, t=0, formato=False):
    res = p - (p * t / 100)
    return res if formato is False else moeda(res)


def dobro(p=0, formato=False):
    res = p * 2
    # se for falso, só mostrara o res sem formatado, sendo verdaderio, mostrara formatado
    return res if not formato else moeda(res)


def metade(p=0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p, a=10, d=5):
    print('_' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('_' * 30)
    print(f'Preço analisado: \t{moeda(p):}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{d}% de redução: \t{diminuir(p, d, True)}')
    print('_' * 30)

