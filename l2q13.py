import unicodedata

def calc_vogais(t):

    t = t.lower()
    t = unicodedata.normalize("NFD",t)
    t = t.encode("ascii","ignore")
    t = t.decode("utf-8")
    t = t.split(" ")
    tam = len(t)
    pontos = 0

    for i in range(tam):
        vogais = 0
        lista_aux = []
        lista_aux = t[i]
        tamanho = len(lista_aux)
        for j in range(tamanho):
            if lista_aux[j] == "a" or lista_aux[j] == "e" or lista_aux[j] == "i" or lista_aux[j] == "o" or lista_aux[j] == "u":
                vogais = vogais + 1
        if vogais%2 == 1:
            pontos+=2
        elif vogais%2 == 0:
            pontos+=1

    pontos = pontos/tam

    return pontos


texto = input("\nDigite um texto: ")

pontuacao = calc_vogais(texto)

print("\nEntrada: {}" .format(texto))
print("Saída: {}\n" .format(pontuacao));