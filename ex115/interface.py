def validar(msg):
    valido = False
    while not valido:
        p = str(input(msg)).strip()
        try:
            int(p)
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favo, digite um número inteiro válido.\033[m')
        else:
            valido = True
    return int(p)


def cabecalho(msg):
    print(linha())
    print(msg.center(40))
    print(linha())


def linha(tam=40):
    return '-' * tam




