def transposta(mat,n,m):
    matriz_t = []
    for i in range(m):
        linha = []
        for j in range(n):
            x = mat[j][i]
            linha.append(x)
        matriz_t.append(linha)
    
    return matriz_t

matriz = []

print("\n")

n = int(input('Digite a quantidade de linhas da matriz: '))
m = int(input('Digite a quantidade de colunas da matriz: '))

print("\n")

for i in range(n):
    linha = []
    for j in range(m):
        x = int(input("Digite o valor de ["+str(i+1)+","+str(j+1)+"]:"))
        linha.append(x)
    matriz.append(linha)

print('\n')
print("Matriz:", matriz)
print("\n")

matriz_transposta = transposta(matriz, n, m)

print("Matriz:", matriz_transposta)
print("\n")