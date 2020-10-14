#Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros. 
#Teste a validade desta data para saber se esta é uma data válida.
dia = int(input('Dia:'))
mes = int(input('Mês:'))
ano = int(input('Ano:'))

if not 1 <= mes <= 12:
    print('O mês está incorreto.')
else:
    if 1 <= dia <= 31:
        if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
            print('ANO BISSEXTO.')
            if mes == 2 and dia >= 29:
                print('Os dias estão corretos.')
            elif mes == [4, 6, 9, 11]:
                if dia >= 30:
                    print('O mês selecionado possui apenas 30 dias.')
            else:
                print('Os dias estão errados.')
        else:
            print('NÃO É ANO BISSEXTO.')
    else:
        print('Dia errado.')