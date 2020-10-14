#Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
valor_venda = float(input('Valor da venda: R$'))
if valor_venda >= 100000:
    com = 700 + (valor_venda * 0.16)
elif valor_venda > 80000:
    com = 650 + (valor_venda * 0.14)
elif valor_venda > 60000:
    com = 600 + (valor_venda * 0.14)
elif valor_venda > 40000:
    com = 550 + (valor_venda * 0.14)
elif valor_venda > 20000:
    com = 500 + (valor_venda * 0.14)
elif valor_venda < 20000:
    com = 400 + (valor_venda * 0.14)
print(f'O valor da comissão será de R${com}.')