#Faça um programa que leia o valor de trabalho em R$ e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
valor = float(input('Valor da hora: R$'))
horas = float(input('Horas:'))
pag = valor * horas
pag_fin = pag + (pag * 0.1)
print(f'O pagamento fica R${pag_fin:.2f}.')