#Faça um programa para ler as dimensões de um terreno, bem como o preço do metro da tela. Imprima o custo para cercar este terreno com tela.
l = float(input('Largura:'))
c = float(input('Comprimento:'))
p = float(input('Preço do metro tela: R$'))
custo = (l + c * 2) * p
print(f'Custo: R${custo:.2f}')