# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
num = int(input('Número:'))
num2 = int(input('Outro número:'))
if num > num2:
    print(f'O número {num} é maior, com a diferença de {num - num2}.')
else:
    print(f'O número {num2} é maior, com a diferença de {num2 - num}.')