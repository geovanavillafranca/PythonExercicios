print('Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:'
      'À vista dinheiro/cheque: 10% de desconto'
      'À vista no cartão: 5% de desconto'
      'Em até 2x no cartão: preço normal'
      '3x ou mais no cartão: 20% de juros')
produto = float(input('Preço das compras: R$'))
print('--------' *6)
print(''' Formas de pagamento e seu desconto:
      \n[1] À vista dinheiro/cheque
      \n[2] À vista no cartão
      \n[3] Em 2x no cartão
      \n[4] 3x ou mais no cartão''')
print('--------' *6)
opcao = int(input('Qual sua escolha? '))
if opcao == 1:
      desc = produto * 10 / 100
      produto = produto - desc
      print('Você tem 10% de desconto, sua compra irá sair por R${:.2f}' .format(produto))
elif opcao == 2:
      desc = produto * 5 / 100
      produto = produto - desc
      print('Você tem 5% de desconto, sua compra irá sair por R${:.2f}'.format(produto))
elif opcao == 3:
      parc = produto / 2
      print('Sua compra será parcelada em 2x de R${:.2f}' .format(parc))
      print('Sua compra irá sair com o preço normal.')
elif opcao == 4:
      qntparc = int(input('Em quantas parcelas? '))
      desc = produto * 20 / 100
      produto = produto + desc
      cadaparc = produto / qntparc
      print('Sua compra será parcelada em {}x de {:.2f} COM JUROS.' .format(qntparc, cadaparc))
      print('Você tem 20% de juros, sua compra irá sair por R${:.2f} total.'.format(produto))
else:
      print('OPÇÃO INVÁLIDA de pagamento. Tente novanmente!')
      print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(produto, produto))







