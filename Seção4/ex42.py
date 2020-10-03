# Receba o salário-base de um funcionário.
# Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário_base.
# Além dissom ele paga 7% de imposto sobre o salário_base.
sal_base = float(input('Salário Base: R$'))
# É fácil verificar que podemos simplificar a equação se subtraimos o valor de gratificação com o de imposto, tendo assim o mesmo resultado.
sal_fin = sal_base + (sal_base * 0.03)
print(f'O salário final será de R${sal_fin:.2f}.')