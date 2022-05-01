dicionario = {}

def incluir_novo_nome(n,t):
    if n in dicionario:
        print("\nO nome já existe na agenda!")
    else:
        lista_de_telefones = []
        lista_de_telefones.append(t)
        dicionario[n] = lista_de_telefones
        print("\nO nome e o telefone foram incluidos na agenda com sucesso!")

def incluir_telefone(n, t):
    if n in dicionario:
        dicionario[n].append(t)
        print("\nO telefone foi incluído com sucesso na agenda!")
    else:
        pergunta = input("\nO nome não existe na agenda. Deseja incluí-lo na agenda? (Sim/Não): ")
        if pergunta == "Sim":
            incluir_novo_nome(n, t)
        else:
            print("\nO nome e o telefone não foram adicionados à lista!")

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
                print("\nO pessoa foi removida da agenda!")
            else:
                print("\nO número foi excluído da agenda!")
        else:
            print("\nNão existe esse telefone na agenda relacionado a pessoa digitada!")
    else:
        print("\nA pessoa não foi encontrada na agenda!")

def excluir_nome(n):
    if n in dicionario:
        dicionario.pop(n)
        print("\nA pessoa foi removida da agenda!")
    else:
        print("\nA pessoa digitada não foi encontrada na agenda!")

def consultar_telefone(n):
    if n in dicionario:
        print("\nNúmeros de {} na lista: " .format(n))
        for t in dicionario[n]:
            print(t)
    else:
        print("\nA pessoa digitada não foi encontrada na agenda!")