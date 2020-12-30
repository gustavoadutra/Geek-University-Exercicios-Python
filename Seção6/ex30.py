#Faça um program para calcular as seguintes sequências:
num = 4
soma2 = soma = soma3 = 0

for x in range(num):
    soma += x

for x in range(2 * num - 1):
    if x % 2 == 0:
        x = -x
    soma2 += x

for x in range(1, 2 * num -1, 2):
    soma3 += x
    
print(soma, soma2, soma3)