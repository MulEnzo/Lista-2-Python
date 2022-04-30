def reverte_agenda(a,n):
    agenda_rever = {}
    tam = 0
    for i in range (n):
        for chave, valor in a.items():
            tam = len(valor)
            while tam>0:
                for i in range(tam):
                    agenda_rever[valor[i]] = chave
                    tam = tam-1

    return agenda_rever


n = int(input('Digite o total de pessoas que a agenda terá: '))

agenda = {}
telefone = []

for i in range(1, n+1):
    continuar = True
    nome = input('\nDigite o nome da {}ª pessoa: '.format(i))
    while nome in agenda:
        print('Erro. Já existe uma pessoa com esse nome cadastrado!')
        nome = input('Nome: ')
    while continuar == True:
        tel = input('Digite o telefone dessa pessoa: ')
        telefone.append(tel)
        resposta = input("Deseja adicionar outro número de telefone para essa pessoa? (s para sim / n para não):  ")
        if resposta == "s":
            continuar = True
        else:
            continuar = False
            agenda[nome] = telefone
            telefone = []

print("\n")
print("Lista original:", agenda)
print("\n")

agenda_rever = reverte_agenda(agenda,n)

print("Lista reversa:", agenda_rever)
print("\n")