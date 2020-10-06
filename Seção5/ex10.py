#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal.
alt = float(input('Altura: [metros]'))
sex = str(input('Sexo: [F/M]'))
if sex in 'Mm':
    print(f'Seu peso ideal seria {72.7 * alt - 58}kg.') 
elif sex in 'Ff':
    print(f'Seu peso ideal seria {62.1 * alt - 44.7}kg.')