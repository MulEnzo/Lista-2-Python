mensagem = input("Digite uma mensagem: ")
print("\nMensagem:",mensagem)

print("\nMensagem depois das mudanças:", end=" ")

for i in mensagem:
    if i == "a" or i == "A":
        print("4", end="")
    elif i == "b" or i == "B":
        print("8", end="")
    elif i == "e" or i == "E":
        print("3", end="")
    elif i == "o" or i == "O":
        print("0", end="")
    elif i == "s" or i == "S":
        print("5", end="")
    elif i == "t" or i == "T":
        print("7", end="")
    else:
        print(i, end="")

print("\n")