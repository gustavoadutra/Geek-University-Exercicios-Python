# Escreva um programa de ajuda para vendedores. Apartir de um valor lido, mostre:
    # O total a pagar com desconto de 10%.
    # O valor de cada parcela, no parcelamento de 3x sm juros.
    # A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto).
    # A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).
valor = float(input('Valor: R$'))
print(f'    =Com 10% de desconto R${valor - (valor * 0.1)}.')
print(f'    =Parcelado em 3x sem juros:\n      R${valor/3}\n      R${valor/3}\n      R${valor/3}')
