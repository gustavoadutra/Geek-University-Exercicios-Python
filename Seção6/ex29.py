#Escreva um programa para calcular o valor da série, para termos.
tot_x = 1
s = 0
for n in range(1, 6):
    for x in range(1, n*2):
        tot_x *= x
    s += n / (tot_x)
print(s)

