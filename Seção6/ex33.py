#Dados n e dois números inteiros positivos, i e j, diferentes de 0m imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
n = 6
i = 2
j = 3
for c in range(0, n):
    if c % i == 0 or c % j == 0:
        print(c, end=',')
print()