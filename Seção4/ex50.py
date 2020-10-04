#Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
from datetime import datetime
now = datetime.now()
#Agora
print(now.hour())
hora = now.hour()
minuto = now.minute()
segundo = now.second()
print(f'{hora}:{minuto}:{segundo}')
print()