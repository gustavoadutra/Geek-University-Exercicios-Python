#Leia uma data e determine se ela é válida.
#Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não são bissextos.
dia = int(input('Dia:'))
mes = int(input('Mês:'))
ano = int(input('Ano:'))
if not 1 <= mes <= 12:
    print('O mês está incorreto.')
else:
    if 1 <= dia <= 31:
        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            print('ANO BISSEXTO.')
            if mes == 2 and dia <= 29:
                print('Os dias estão corretos.')
            else:
                print('Os dias estão errados.')
        else:
            print('NÃO É ANO BISSEXTO.')
    else:
        print('Dia errado.')


    
