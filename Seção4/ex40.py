# Uma empresa contrata um encanador a R$30,00 por dia. 
# Faça um programa que solicite p número dos dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga. 
# Sabendo-se que são descontados 8% para o imposto de renda.
dias_trabalhados = float(input('Quantos dias foram trabalhados?'))
desc = dias_trabalhados * 30 * 0.08
pagamento = 30 * dias_trabalhados - desc
print(f'O pagamento será de R${pagamento:.2f} já realizando o desconto de R${desc:.2f}.')