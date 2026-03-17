mediaList = []

def listaNotasValid(listaNotas):
    for i in range(len(listaNotas)):
        if (type(listaNotas[i]) == str or listaNotas[i] <= -1):
            #print(f"False, {listaNotas[i]}")
            return False, listaNotas[i]
        else: 
            continue

    #print(f"True, {listaNotas}")
    return True


def calcMedia(listaNotas):
    print(f"{listaNotas}")
    notaSum = 0
    aprov = ""

    if (listaNotasValid(listaNotas) == True):
        for i in range(len(listaNotas)):
            notaSum += listaNotas[i]
        media = notaSum / len(listaNotas)

        if (media < 7.0):
            aprov = "REPROVADO"
        else: aprov = "APROVADO"

        return media, aprov
    else:
        print(f" - Lista de notas inválida. \n Corrija as pendências e tente novamente. ")
        print(f" dumpErro: {listaNotasValid}, {listaNotas}") #Ops, ele escreve o endereço de memória em que o erro ocorre....
    print(f"Corrija os erros na lista de notas, e tente novamente.")



#def rankAluno(mediaList):
