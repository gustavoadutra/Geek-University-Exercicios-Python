# Escreva um programa de ajuda para vendedores. Apartir de um valor lido, mostre:
    # O total a pagar com desconto de 10%.
    # O valor de cada parcela, no parcelamento de 3x sem juros.
    # A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto).
    # A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).

valor = float(input('Valor: R$'))
desc = valor - (valor * 0.1)
parc = valor/3
comis_vista = desc - (desc * 0.05)
comis_parc = valor + (valor * 0.05)
print(f'    = Com 10% de desconto R${desc:.2f}.')
print(f'    = Parcelado em 3x sem juros:\n      R${parc:.2f}\n      R${parc:.2f}\n      R${parc:.2f}')
print(f'    = A comissão do vendedor, com 5% de desconto a vista fica R${comis_vista:.2f}')
print(f'    = A comissão do vendedo, com 5% de aumento se parcelado R${comis_parc:.2f}.')