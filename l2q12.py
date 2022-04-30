def sublista(lista_1,lista_2):
    lista_auxiliar = []
    for i in range(len(lista_2)):
        if lista_2[i] in lista_1:
            lista_auxiliar.append(lista_2[i])

    if lista_1 == lista_auxiliar:
        return True
    else:
        return False

l1 = []
l2 = []

n = int(input("\nDigite quantos elemento a lista 1 terá: "))

for i in range(n):
    k = int(input("\nDigite o {}° elemento da lista 1: " .format(i+1)))
    l1.append(k)

m = int(input("\nDigite quantos elemento a lista 2 terá: "))

for i in range(m):
    j = int(input("\nDigite o {}° elemento da lista 1: " .format(i+1)))
    l2.append(j)

retorno = sublista(l1,l2)

print("\n")
if retorno == True:
    print("{} é uma sublista de {}" .format(l1, l2))
else:
    print("{} não é uma sublista de {}" .format(l1, l2))
print("\n")