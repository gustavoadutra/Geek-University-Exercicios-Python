#Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma

val = val2 = 0

for num in range(0, 101):
    val += num ** 2
    val2 += num
    
tot = val - (val2 ** 2)
print(tot)