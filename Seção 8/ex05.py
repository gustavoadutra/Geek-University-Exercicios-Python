#Faça uma função e um programa de teste para cálculodo volume de uma esfera.
#Ve = 4/3 * pi * R ** 3

def volume_esfera(raio):
    ve = 4/3 * 3 * raio ** 3
    print(ve, 'm3 da esfera.')
def volume_cilindro(raio, altura):
    vc = 3.14 * altura * raio ** 2
    print(vc, 'm3 do cilindro.')

volume_esfera(5)
volume_cilindro(4, 5)
