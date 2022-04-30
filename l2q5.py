p = []

print("\n")

n = int(input("Digite o número de pontuações do atleta: "))

print("\n")

for i in range(n):
    k = int(input("Digite a pontuação {} do atleta nos seus jogos: " .format(i+1)))
    p.append(k)

max = p[0]
min = p[0]
p_max = 0
p_min = 0

for i in p:
    if i > max:
        max = i
        p_max+=1
    elif i < min:
        min = i
        p_min+=1

print("\n\n-------Dados da pontuação dos atletas-------\n")
print("p_max = {} e p_min = {}" .format(p_max,p_min))
print("\n")