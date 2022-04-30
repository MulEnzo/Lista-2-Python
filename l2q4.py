l1 = []
l2 = []

p_a1 = 0
p_a2 = 0

n = int(input("Digite o tamanho das listas: "))

print("\n")

for i in range(n):
    k = float(input("Digite a nota {} do aluno 1: " .format(i+1)))
    l1.append(k)
    l = float(input("Digite a nota {} do aluno 2: " .format(i+1)))
    l2.append(l)

for i in range(n):
    if l1[i] > l2[i]:
        p_a1+=1
    elif l2[i] > l1[i]:
        p_a2+=1

print("\n-------Pontuação dos alunos-------\n")
print("p_a1 = {} e p_a1 = {}" .format(p_a1,p_a2))
print("\n")