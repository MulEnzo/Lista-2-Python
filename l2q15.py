def teste_cnpj(cnpj):

    cnpj_1_12 = []
    soma = 0
    lista_multiplicador = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3 ,2]
    d1 = 0
    d2 = 0

    for i in range(12):
        cnpj_1_12.append(cnpj[i])

    print(cnpj)
    print(cnpj_1_12)

    for i in range(12):
        x = (cnpj_1_12[i])*(lista_multiplicador[i])
        soma = soma + x
    y = soma%11

    if y<2:
        d1 = 0
    else:
        d1 = 11-y

    soma = 0
    lista_multiplicador = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3 ,2]
    cnpj_1_13 = cnpj_1_12
    cnpj_1_13.append(d1)

    for i in range(13):
        k = (cnpj_1_12[i])*(lista_multiplicador[i])
        soma = soma + k
    l = soma%11

    if y<2:
        d2 = 0
    else:
        d2 = 11-l

    if d1 == cnpj[-2] and d2 == cnpj[-1]:
        return True
    else:
        return False


cnpj = input("\nDigite o número do CNPJ: ")

cnpj = list(cnpj)
tam = len(cnpj)

if len(cnpj) == 14:
    retorno = teste_cnpj(cnpj)
else:
    print("\nO número digitado não tem as dimensões corretas!")

'''print(retorno)'''