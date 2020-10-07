# Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas(as básicas, por exemplo). 
# O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
print('Menu:')
print('(1)Somar\n(2)Subtrair\n(3)Dividir\n(4)Multiplicar')
escolha = int(input('Escolha:'))
if escolha == 1:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A soma equivale a {num1 + num2}.')
elif escolha == 2:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A subtração equivale a {num1 - num2}.')
elif escolha == 3:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A divisão equivale a {num1 / num2}.')
elif escolha == 4:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A multiplicação equivale a {num1 * num2}.')
