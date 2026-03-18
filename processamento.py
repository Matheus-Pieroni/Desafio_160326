mediaList = []

def listaNotasValid(listaNotas):
    if (len(listaNotas) != 0):
        for i in range(len(listaNotas)):
            if (type(listaNotas[i]) == str or listaNotas[i] <= -1):
                #print(f"False, {listaNotas[i]}")
                return False, listaNotas[i]
            else: 
                continue

        #print(f"True, {listaNotas}")
        return True
    else: print(f"Lista Inválida de Notas, tente novamente.")


def calcMedia(listaNotas, aluno):
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
            
        '''
            Aqui vem uma questão interessante, a cada iteração, o próprio py pode passar em que posição o aluno está
            e então eu utilizo para repassar a informação de volta para a lista original.
        '''
        mediaList.append([aluno, media])
        return media, aprov
    else:
        print(f" - Lista de notas inválida. \n Corrija as pendências e tente novamente. ")
        print(f" dumpErro: {listaNotasValid}, {listaNotas}") #Ops, ele escreve o endereço de memória em que o erro ocorre....
    print(f"Corrija os erros na lista de notas, e tente novamente.")

'''
 Aqui a gente adiciona o sistema de ranking de alunos ao retornar exatamente 3 parâmetros. >> Nesse caso a media, se o aluno foi aprovado e uma lista contendo as medias.

 Depois a gente recebe essa lista na função rankAluno() que vai organiza-la em ordem decrescente, e trazer o nome dos alunos correspondentes.
'''

def rankAlunos():
    print(f"\n\t × RANKING DE ALUNOS: × ")
    print(f"Lista Original de Médias.")
    for i in range(len(mediaList)):
        print(f"Aluno: {mediaList[i][0]}, Média: {mediaList[i][1]}\n")

    reorderMediaList = sorted(mediaList, key=lambda tup: tup[1], reverse = True)
    '''
    i = len(mediaList) - 1 # Pego a lista completa
    print(i)
    # Vamos ordenar de trás pra frente.
    while i != 0:   # Se a contagem chegar a zero pare.
        valor1 = mediaList[i] 
        valor2 = mediaList[i-1]
        if (valor1 < valor2):
            mediaList[i] = valor1
            mediaList[i-1] = valor2
        i -= 1
    '''

    print(f"\n « Posições Finais! »")
    for i in range(len(reorderMediaList)):
        print(f"\t{i+1}° - {reorderMediaList[i][0]} × MÉDIA FINAL - {reorderMediaList[i][1]}\n")