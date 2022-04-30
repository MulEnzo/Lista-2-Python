def codificar(s):

    s = list(s)

    alf_imp = ["a","c","e","g","i","k","m","o","q","s","u","w","y"]
    alf_par = ["b","d","f","h","j","l","n","p","r","t","v","x","z"]
    alf_imp_mai = ["A","C","E","G","I","K","M","O","Q","S","U","W","Y"]
    alf_par_mai = ["B","D","F","H","J","L","N","P","R","T","V","X","Z"]
    
    tam_str = len(s)
    tam_alf = len(alf_imp)

    for i in range(tam_str):
        for j in range(tam_alf):
            if s[i] == alf_imp[j]:
                s[i] = alf_par[j]
            elif s[i] == alf_par[j]:
                s[i] = alf_imp[j]
            elif s[i] == alf_imp_mai[j]:
                s[i] = alf_par_mai[j]
            elif s[i] == alf_par_mai[j]:
                s[i] = alf_imp_mai[j]

    return s


string = input("\nDigite uma string: ")

print("\n")
print("String:", string)
print("\n")

string_codificada = (codificar(string))

str = "".join(string_codificada)

print("String codificada:", str)
print("\n")