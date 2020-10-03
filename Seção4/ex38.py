#Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
sal = float(input('Valor:'))
desc = sal + (sal * 0.25)
print(f'Com o aumento temos R${desc}.')