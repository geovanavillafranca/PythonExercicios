print('Refaça o DESAFIO 009, mostrando um número que o usuário escolher, só que agora utilizando um laço for.')
n = int(input('Digite um número inteiro: '))
for c in range(1,11):
    a = c * n
    print(c, ' * ', n, ' = ', a)
