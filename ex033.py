print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite o ultimo número: '))
print('---' *10)
if (num1 > num2) and (num1 > num3):
    print('O número maior é o {}' .format(num1))
elif (num2 > num1) and (num2 > num3):
    print('O número maior é o {}' .format(num2))
else:
    print('O número maior é o {}' .format(num3))
print('---' *10)
if (num1 < num2) and (num1 < num2):
    print('E o número menor é o {}' .format(num1))
elif (num2 < num1) and (num2 < num3):
    print('E o número menor é o {}' .format(num2))
else:
    print('E o número menor é o {}' .format(num3))
print('---' *10)
