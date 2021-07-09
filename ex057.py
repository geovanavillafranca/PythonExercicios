print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.'
      'Caso esteja errado, peca a digitação novamente até ter um valor correto.')

sexo = str(input('Digite seu sexo [F/M]: ')).strip().lower()[0]
while sexo not in 'fm':
      sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().lower()[0]
print('Sexo {} registrado com sucesso.' .format(sexo.upper()))

