#Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo de serviço de cada funcionário.
sal = float(input("Salário: R$"))
tempo = float(input('Anos trabalhados:'))
if tempo < 1:
    print('Sem bonus!')
elif tempo <= 3:
    print('Bônus R$100,00')
elif tempo <= 6:
    print('Bônus R$200,00')
elif tempo <= 10:
    print('Bônus R$300,00')
elif tempo > 10:
    print('Bônus R$500,00')
if sal <= 500:
    sal_reaj = sal + sal * 0.25
elif sal <= 1000:
    sal_reaj = sal + sal * 0.2
elif sal <= 1500:
    sal_reaj = sal + sal * 0.15
elif sal <= 2000:
    sal_reaj = sal + sal * 0.1
elif sal > 2000:
    sal_reaj = sal
print(f'O salário será de R${sal_reaj:.2f}.')

