def teste_cnpj(cnpj):

    cnpj_1_12 = []
    cnpj_1_13 = []
    cnpj_1_14 = []
    lista_multiplicador1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3 ,2]
    lista_multiplicador2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3 ,2]
    soma = 0
    d1 = 0
    d2 = 0

    for i in range(12):
        z = int((cnpj[i]))
        cnpj_1_12.append(z)

    for i in range(12):
        x = (cnpj_1_12[i])*(lista_multiplicador1[i])
        soma = soma + x
    y = soma%11
    if y<2:
        d1 = 0
    else:
        d1 = 11-y

    cnpj_1_13 = cnpj_1_12
    cnpj_1_13.append(d1)
    soma = 0

    for i in range(13):
        k = (cnpj_1_13[i])*(lista_multiplicador2[i])
        soma = soma + k
    l = soma%11
    if l<2:
        d2 = 0
    else:
        d2 = 11-l

    cnpj_1_14 = cnpj_1_13
    cnpj_1_14.append(d2)

    cnpj_final = ''
    for i in range(len(cnpj_1_14)):
        cnpj_final+=str(cnpj_1_14[i])

    if cnpj == cnpj_final:
        return True
    else:
        return False


cnpj = input("\nDigite o CNPJ (apenas os números): ")

tam = len(cnpj)

if tam == 14:
    retorno = teste_cnpj(cnpj)
else:
    print("\nO número digitado não tem as dimensões corretas!")

if retorno == True:
    print("\nEste é um CNPJ aceito!\n")
else:
    print("\nEste não é um CNPJ aceito!\n")