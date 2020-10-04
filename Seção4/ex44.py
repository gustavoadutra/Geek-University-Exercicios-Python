#Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
alt_deg = float(input('Altura do degrau:'))
alt = float(input('Qual é altura desejada?'))
resul = alt / alt_deg
print(f'Será necessário subir {resul} degraus.')