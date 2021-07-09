print('Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário'
      'com as seguintes informações:'
      '- quantidade de notas'
      '- a maior nota'
      '- a menor nota'
      '- a média da turma'
      '- a situação(opcional)'
      'Adicione também os docstringss da função')


def notas(*num, sit=False):
      """
      -> Função para analisar notas e situações de vparios alunos.
      :param n: uma ou mais notass dos alunos (aceita várias)
      :param sit: valor opcional, indicando se deve ou não adicionar a situação
      :return: dicionário com várias informações sobre a situação da turma.
      """
      n = {}
      n['total'] = len(num)
      n['maior'] = max(num)
      n['menor'] = min(num)
      n['média'] = sum(num) / len(num)
      if sit:
            if n['média'] >= 7:
                  n['situação'] = 'BOA'
            elif n['média'] >= 5:
                  n['situação'] = 'RAZOÁVEL'
            else:
                  n['situação'] = 'RUIM'
      return n


# Programa Principal
resp = notas(9, 10, 6.5, 10, sit=True)
print(resp)



