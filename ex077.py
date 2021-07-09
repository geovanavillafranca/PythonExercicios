(print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos. '
       'Depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.'))

palavras = ('Papagaio', 'Banana', 'Geovana', 'Computador')
# O p vai buscar cada palavra e printar, uma de cada vez
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    # com a letra, podemos pegar por cada palavra e identificar suas vogais em uma condição:
    for letra in p:
        # Se em letra(cada palavra) conter 'aeiou', ele irá mostrar quais são:
        if letra in 'aeiou':
            print(letra.lower(), end=' ')
