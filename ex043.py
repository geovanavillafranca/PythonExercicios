print('Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:'
      'Abaixo de 18.5: Abaixo do Peso'
      'Entre 18.5 a 25: Peso ideal'
      '25 até 30: Sobrepeso'
      '30 até 40: Obesidade'
      'Acima de 40: Obesidade mórbida')
print('---' *4 + ' CALCULO DE IMC ' + '---' *4)
peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print('O seu IMC é \033[1;34m {:.2f} \033[m.' .format(imc))
if imc < 18.5:
      print('Você está \033[4;35mabaixo\033[m do peso.')
elif 18.5 <= imc < 25:
      print('Você está com o peso ideal.')
elif 25 <= imc < 30:
      print('Você está com \033[0;33msobrepeso\033[m.')
elif 30 <= imc < 40:
      print('Você está com \033[0;0;43mobesidade\033[m.')
elif imc >= 40:
      print('Você está com \033[1;0;41mobesidade mórbida\033[m.')
