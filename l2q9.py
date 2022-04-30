def eh_palindroma(p,t):
    p2 = p
    soma = 0
    for i in range(t):
        if p[i] == p2[-i-1]:
            soma+=1

    if soma == t:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")

tam = len(palavra)
palavra = palavra.lower()

eh = eh_palindroma(palavra,tam)

print("\n")
print("A palavra é Palíndroma: ", eh)
print("\n")