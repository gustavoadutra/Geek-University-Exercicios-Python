# Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
# Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
sal = float(input('Salário: R$'))
prest = float(input('Prestação: R$'))
if prest / sal < 0.2:
    print('Empréstimo concedido.')
else: 
    print('Empréstimo não concedido.')