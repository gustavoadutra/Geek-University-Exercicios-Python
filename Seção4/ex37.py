#Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
valor = float(input('Valor:R$'))
desc = valor - (valor * 0.12)
print(f'O valor com deconto de 12% fica R${desc}.')