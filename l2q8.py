def verificacao(l,s):
    eh_true = False
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==s and i!=j:
                eh_true = True
    return eh_true

lista = []

print("\n")

n = int(input("Digite o tamanho da lista de números inteiros: "))

print("\n")

for i in range(n):
    k = int(input("Digite {}° número inteiro dessa lista: " .format(i+1)))
    lista.append(k)

soma = int(input("Digite o valor da soma: "))

eh_verdade = verificacao(lista,soma)

print("\n")
print(eh_verdade)
print("\n")