import funcoesl2q14

opcao = 0

while opcao!=6:

    print("\n------ Menu Agenda ------")
    print("\n1 – Incluir novo nome\n2 – Incluir telefone\n3 – Excluir telefone\n4 – Excluir nome\n5 - Consultar telefone\n6 - Sair\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome que deseja incluir na agenda: ")
        tel = int(input("Digite o telefone dessa pessoa: "))
        funcoesl2q14.incluir_novo_nome(nome, tel)

    elif opcao == 2:
        nome = input("Digite o nome da pessoa dona do telefone: ")
        tel = int(input("Digite o telefone dessa pessoa: "))
        funcoesl2q14.incluir_telefone(nome, tel)

    elif opcao == 3:
        nome = input("Digite o nome da pessoa que você deseja excluir o telefone: ")
        tel = int(input("Digite o telefone que deseja excluir dessa pessoa: "))
        funcoesl2q14.excluir_telefone(nome, tel)

    elif opcao == 4:
        nome = input("Digite o nome da pessoa que deseja excluir da lista: ")
        funcoesl2q14.excluir_nome(nome)

    elif opcao == 5:
        nome = input("Digite o nome da pessoa que deseja consultar o telefone: ")
        funcoesl2q14.consultar_telefone(nome)

    elif opcao == 6:
        print("\nSaindo do programa ... \n")

    else:
        print("\nOpção Inválida. Tente novamente\n")