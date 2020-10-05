# Faça um programa que receba dois números e mstre o maior.
# Se por acaso, os dois números forem iguais, imprima a mensagem Números Iguais.
num1 = int(input('Número 1:'))
num2 = int(input('Número 2:'))
if num1 > num2:
    print(f'O número {num1} é maior.')
elif num1 < num2:
    print(f'O número {num2} é maior.')
elif num1 == num2:
    print('Os Números são Iguais.')