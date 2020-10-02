#Leia um número inteiro e imprima a soma do seu sucessor de seu triplo com o antecessor de seu dobro.
num = int(input('Valor:'))
print(f'{((num + 1)*3) + ((num - 1)*2)}')