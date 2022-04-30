import math

notas = []
var = 0.0
mediana = 0
moda = []
rep = 0

print("\n")

while True:
    avaliacao = int(input("Digite uma nota para a qualidade da comida do refeitório de 1-5 (1-Péssimo / 5-Excelente): "))
    if avaliacao>=1 and avaliacao<=5:
        notas.append(avaliacao)
    else:
        break

notas_sem_repetir = set(notas)
notas.sort()
media = sum(notas)/len(notas)

for i in notas_sem_repetir:
    if notas.count(i) > rep:
        rep = notas.count(i)
        while len(moda) > 0:
            moda.pop(0)
        moda.append(i)
    elif notas.count(i) == rep:
        moda.append(i)

if len(notas)%2 != 0:
    mediana = notas[(len(notas)//2)]
else:
    mediana = (notas[(len(notas)//2)-1] + notas[len(notas)//2])/2

for i in range(len(notas)):
    var+= (notas[i]-media)**2

var = var/len(notas)
dp = math.sqrt(var)

print("\n")

for i in notas_sem_repetir:
    print("Nota: {} - Frequência: {}" .format(i,notas.count(i)))

print("\n-------Estatísticas das resposta lidas-------\n")

print("Valor mínimo:", min(notas))
print("Valor máximo:", max(notas))
print("Valor médio: {:.2f}" .format(media))
print("Mediana: {:.2f}" .format(mediana))
print("Moda:", moda)
print("Variância: {:.2f}" .format(var))
print("Desvio padrão: {:.2f}" .format(dp))
print("\n")