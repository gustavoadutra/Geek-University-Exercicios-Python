#Faça uma função que receba dois números e retorne qual deles é o maior.

def maior(val1, val2):
    if val1 > val2:
        maior = val1
    elif val2 > val1:
        maior = val2
    return maior


print(maior(3, 3))