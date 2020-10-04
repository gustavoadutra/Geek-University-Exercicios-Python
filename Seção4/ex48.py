#Leia um valor inteiro em segundos, imprima ele em horas e minutos.
seg = int(input('Segundos:'))
minu = seg / 60
horas = minu / 60
print(f'Em horas: {horas:.3f}, em minutos {minu:.2f}.')