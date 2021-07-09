print('Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.')

for c in range(1,51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

# um jeito mais facil que consome menos é:
# ele ja vai fazer pulando de dois em dois, fica mais pratico e nao precisa do IF
for c in range(2, 51, 2):
    print(c, end='  ')
print('FIM')

