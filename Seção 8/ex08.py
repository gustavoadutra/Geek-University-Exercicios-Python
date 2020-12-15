#Sejam a e b os catetos de um triângulo, faça uma função que calcule o valor da hipotenusa, recebendo o valor dos catetos a e b.


def hipotenusa(a, b):
    hipo = ((a ** 2) + (b ** 2)) ** 1/2
    return  hipo


print(hipotenusa(3,4))