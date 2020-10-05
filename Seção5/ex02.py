# Leia um número fornecido pelo usuário. 
# Se esse número for positivo, calcule a raiz quadrada. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é válido.
num = float(input('Número:'))
if num % 2 != 0:
    print(f'O número {num} é impar.')
    print('O número é inválido.')
else:
    resul = num ** 1/2
    print(f'O número {num} é par, sua raiz quadrada é {resul}.')