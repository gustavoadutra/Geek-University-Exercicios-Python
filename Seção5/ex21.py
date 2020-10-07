# Escreva um menu de opções. Leia a opção do usuário e execute a operção escolhida. 
# Escreva uma mensagem de erro se a opção for inválida.
print('Escolha a Opção:')
print('1- Somar.')
print('2- Subtrair do menor para o maior.')
print('3- Divisão o denomindador deve ser diferente de zero.')
print('4- Multiplicar.')
opç = int(input('Opção:'))
if opç == 1:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A soma equivale a {num1 + num2}.')
elif opç == 2:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    if num1 > num2:
        resul = num1 - num2
    else:
        resul = num2 - num1
    print(f'O resultado da subtração é {resul}.')
elif opç == 3:
    num2 = int(input('Número:'))
    num1 = int(input('Denominador:'))
    if num2 <= 0:
        print('O denominador é 0 ou menor que o mesmo.\n ERROR')
    else:
        print(f'A divisão equivale a {num1 / num2}.')
elif opç == 4:
    num1 = int(input('Número:'))
    num2 = int(input('Número:'))
    print(f'A multiplicação equivale a {num1 * num2}.')