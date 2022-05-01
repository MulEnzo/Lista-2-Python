dicionario = {}

def incluir_novo_nome(n,t):
    lista_de_telefones = []
    lista_de_telefones.append(t)
    dicionario[n] = lista_de_telefones
    print("\nO nome com o seu repectivo número foi incluido na agenda com sucesso\n")

def incluir_telefone(n, t):
    if n in dicionario:
        dicionario[n].append(t)
        print("\nO telefone foi incluído com sucesso na agenda\n")
    else:
        pergunta = input("O nome não existe na agenda. Deseja incluí-lo na agenda? (Sim/Não): ")
        if pergunta == "Sim":
            incluir_novo_nome(n, t)

def excluir_telefone(n, t):
    if n in dicionario:
        lista_numeros = dicionario[n]
        tamanho = len(lista_numeros)
        if t in lista_numeros:
            lista_adicionar = []
            dicionario.pop(n)
            for i in range(tamanho):
                if lista_numeros[i] != t:
                    lista_adicionar.append(lista_numeros[i])
            dicionario[n] = lista_adicionar
            if len(lista_adicionar) <= 0:
                dicionario.pop(n)
                print("\nO nome foi apagado da agenda\n")
            else:
                print("\nO número foi excluído\n")
        else:
            print("\nNão existe esse telefone relacionado a pessoa digitada\n")
    else:
        print("\nA pessoa não foi encontrada na agenda\n")

def excluir_nome(n):
    if n in dicionario:
        dicionario.pop(n)
        print("\nA pessoa foi removida da agenda\n")
    else:
        print("O nome digitado não foi encontrado na agenda\n")

def consultar_telefone(n):
    if n in dicionario:
        for t in dicionario[n]:
            print("Números dessa pessoa: ", end="")
            print(t)
    else:
        print("O nome digitado não foi encontrado na agenda\n")