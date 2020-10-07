#Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
num = int(input('Número:'))
if num <= 0:
    print('Número Inválido.')
else:    
    val1 = int(str(int(num / 1000))[-1])
    val2 = int(str(int(num / 100))[-1])
    val3 = int(str(int(num / 10))[-1])
    val4 = int(str(int(num / 1))[-1])
    val_fin = val1 + val2 + val3 + val4
    print(val_fin)