#Faça  um algoritmo que calcule a média ponderada das notas de 3 provas.
#A primeira e a segunda prova têm peso 1 e a terceira tem peso 2.
#Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

nota1 = int(input('1- Nota:'))
nota2 = int(input('2- Nota:'))
nota3 = int(input('3- Nota:'))

med_pond = (nota1 + nota2 + nota3 * 2)/3
print(med_pond)