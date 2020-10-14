#Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
med = med_fin = 0
for num in range(0, 10):
    med = int(input(f'{num}- Número:'))
    if num % 2 == 0:
        med_fin += med 
print(f'Média = {med / 10}')