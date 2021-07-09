from ex115.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        # gravacao de arquivo texto, cria caso n exista +
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def verPessoas(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(arq.read())
        arq.close()


def cadastro(arq, nome='desconhecido', idade=0):
    try:
        # abrir o arquivo para depois poder cadastrar as pessoas
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            # tentando cadastrando as pessoas
            a.write(f'{nome};{idade}\n')
            a.close()
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            #cadastro deu certo, agora fecha o arquivo
            print(f'Novo registro de {nome} cadastrado com sucesso!')
            a.close()
