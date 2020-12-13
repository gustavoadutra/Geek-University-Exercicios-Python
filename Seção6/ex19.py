#Escreva um algoritmo que leia um número entre 100 e 999 e imprima em sua saída cada um dos algarismos que compôem o número.
num = int(input('Número:'))
if 100 < num < 999:
    for n in str(num):
        print(n)
else:
    print("Digite um número de 100 a 999.")