from ex115.lib.arquivo import *
from interface import *
from time import sleep

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

dicionario = {'1': 'Ver pessoas cadastradas',
              '2': 'Cadastrar nova Pessoa',
              '3': 'Sair do Sistema'}
while True:
    cabecalho('MENU PRINCIPAL')
    for k, v in dicionario.items():
        print(f'\033[33m{k}\033[m - ', end='')
        print(f'\033[34m{v}\033[m')
    print('-' * 40)
    escolha = validar('\033[32mSua opção: \033[m')
    print('-' * 40)
    if escolha == 1:
        verPessoas(arq)
        sleep(1)
    elif escolha == 2:
        cabecalho('CADASTRANDO UMA PESSOA')
        nome = str(input('Nome: '))
        idade = validar('Idade: ')
        cadastro(arq, nome, idade)
        sleep(1)
    elif escolha == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(.5)
