print('Faça um programa que leia uma frase pelo teclado e mostre:'
      '1- Quantas vezes aparece a letra "A".'
      '2- Em que posição ela aparece a primeira vez.'
      '3- Em que posição ela aparece a última vez.')
frase = str(input('Digite uma frase: ').lower().strip())
print('Nessa frase a letra A aparece {} vezes.' .format(frase.count('a')))
print('Ela aparece na posição {}.' .format(frase.find('a')+1))
print('Ela aparece pela última vez {}.' .format(frase.rfind('a')+1))
