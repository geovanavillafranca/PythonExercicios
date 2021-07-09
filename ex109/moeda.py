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

