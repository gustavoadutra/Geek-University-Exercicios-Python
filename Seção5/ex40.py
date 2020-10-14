#O custo do consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor e dos impostos.
custo_fab = float(input('Custo de fábrica: R$'))
if custo_fab <= 12000:
    preço_fin = custo_fab + (custo_fab * 0.05) + (custo_fab * 0)
if custo_fab <= 25000:
    preço_fin = custo_fab + (custo_fab * 0.1) + (custo_fab * 0.15) 
if custo_fab > 25000:
    preço_fin = custo_fab + (custo_fab * 0.15) + (custo_fab * 0.2)

print(f'O valor será de R${preço_fin:.2f}.')