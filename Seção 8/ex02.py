#Faça um programa que receba a data atual e exiba-a na tela no formato textual por extenso.

lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def conversor(dia, mes, ano):
    
    mes_extenso = lista_meses[mes - 1]
    print(f'{dia} de {mes_extenso} de {ano}.')
conversor(8, 1, 2003)