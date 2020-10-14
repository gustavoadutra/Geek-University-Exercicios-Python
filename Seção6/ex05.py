#Faça um programa que peça ao usuário para digitar 10 valores e some-os.
soma = 0
for num in range(0, 10):
    soma += int(input(f'{num}- Número:'))
print(f'Soma = {soma}')