#Ler um número inteiro. Se o número lido for negativo, escreva uma mensagem "Número inválido".
#Se o número for positivo, calcular o logaritmo deste número.
num = int(input('Número:'))
if num < 0:
    print('Número Inválido.')
else:
    base = int(input('Base:'))
    b = base ** num
    print(f'O logaritmando resultante será {b}.')