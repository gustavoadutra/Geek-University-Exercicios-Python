# Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas.
# Uma nota válida deve ser, obrigatoriamente, um valor entre 0 e 10, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa imprima.
nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
if nota1 <= 0 or nota1 >= 10 and nota1 <= 0 or nota1 >= 10:
    print('Não, a nota está digitada erroneamente.')
else:
    print(f'A média tirada foi {(nota1 + nota2)/2}')