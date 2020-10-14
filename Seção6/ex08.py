#Escreva um programa que leia 10 números e escreva menor número e o maior valor lido.
for num in range(0, 10):
    num_s = int(input(f'{num}- Número:'))
    if num == 0:
        maior = menor = num_s
    if num_s > maior:
        maior = num_s
    elif num_s < menor:
        menor = num_s
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')