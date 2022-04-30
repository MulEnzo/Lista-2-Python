def matriz_quadrada(mat,n):
    
    soma_linha=[]
    soma_coluna=[]
    soma_diag_prin=[]
    soma_diag_sec=[]
    soma_l=0
    soma_c=0
    soma_dp=0
    soma_ds=0

    for i in range(n):
        for j in range(n):
            soma_l+=mat[i][j]
        soma_linha.append(soma_l)
        soma_l=0

    for j in range(n):
        for i in range(n):
            soma_c+=mat[i][j]
        soma_coluna.append(soma_c)
        soma_c=0

    for i in range(n):
        for j in range(n):
            if i==j:
                soma_dp+=mat[i][j]
    soma_diag_prin.append(soma_dp)

    
    for i in range(n):
        for j in range(n):
            if i+j == n-1:
                soma_ds+=mat[i][j]
    soma_diag_sec.append(soma_ds)

    soma_linha = set(soma_linha)
    soma_coluna = set(soma_coluna)
    soma_diag_prin = set(soma_diag_prin)
    soma_diag_sec = set(soma_diag_sec)

    if soma_linha == soma_coluna == soma_diag_prin == soma_diag_sec:
        print("Essa Matriz Quadrada é um Quadrado Mágico\n")
    else:
        print("Essa Matriz Quadrada não é um Quadrado Mágico\n")

matriz = []

print("\n")

n = int(input('Digite a quantidade de linhas e colunas da matriz: '))

print("\n")

for i in range(n):
    linha = []
    for j in range(n):
        x = int(input("Digite o valor de ["+str(i+1)+","+str(j+1)+"]:"))
        linha.append(x)
    matriz.append(linha)

print('\n')
print("Matriz:", matriz)
print("\n")

matriz_quadrada(matriz,n)