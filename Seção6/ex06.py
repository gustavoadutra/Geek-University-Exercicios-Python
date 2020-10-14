#Faça um programa que leia 10 inteiros e imprima sua média.
med = 0
for num in range(0, 10):
    med += int(input(f'{num}- Número:'))
print(f'Média = {med / 10}')