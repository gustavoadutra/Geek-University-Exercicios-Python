#Faça um programa que some os números impares contidos em um intervalo definido pelo usuário.
#O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números impares contidos nesse intervalo.
x = int(input('Valor:'))
y = int(input('Valor:'))
soma = 0
if x >= y:
    print('Valor inválido.')
else:
    for n in range(x, y):
        if n % 2 != 0:
            print(n)
            soma += n
            
    print('A soma será igual a', soma)