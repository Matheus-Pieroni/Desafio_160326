import processamento as procc

alunos = []
# Lista error proof
aluno0 = [("Jorge"), ([8, 7, 5, 9, 6])]
aluno1 = [("Maikon"), ([8, 8, 7, 6, 4])]
aluno2 = [("Séphey"), ([6, 9, 4, 8, 7])]
aluno3 = [("Raphael"), ([6, 6, 7, 4, 9])]
aluno4 = [("Cléberc"), ([5, 6, 7, 8, 9])]

# Lista error for sure >:)
aluno5 = [("Jorge"), ([8, 6, 5, 9, 6])]
aluno6 = [("Séphey"), ([6, 9, 4, ":D", 7])]
aluno7 = [("Raphael"), ([6, False, 7, 4, 9])]
aluno8 = [("Cléberc"), ([5, 6, 7, 8, 9])]
aluno9 = [("Maikon"), ([8, "ai", 7, 6, 4])] # Vai parar aqui... teoricamente

nomProf = input(f"Logar como: (Nome do Professor)\n >>")
ranking = []

print(f" «« Bem-vindo professor {nomProf}. »» ")

resp = 3
while (resp != 0):
    resp = int(input(f"Selecione a lista que quer utilizar \n\t 1 - Lista Limpa \n\t\t OU \n\t 2 - 'Lista Suja'? \n >>"))

    if (resp == 1):
        print(f"Utilizando a lista limpa -»» ")
        alunos.append(aluno0)
        alunos.append(aluno1)
        alunos.append(aluno2) 
        alunos.append(aluno3) # Adiciono alunos de teste
        alunos.append(aluno4)
        print(f"{len(alunos)} Alunos adicionados")
        resp = 0
    elif (resp == 2):
        print(f"Utilizando a lista suja -»» ")
        alunos.append(aluno4)
        alunos.append(aluno5)
        alunos.append(aluno6) 
        alunos.append(aluno7) # Adiciono alunos de teste
        print(f"{len(alunos)} Alunos adicionados")
        resp = 0
    else: print(f"Opção inválida selecionada tente novamente")

# É como se eu fizesse uma lista 2D, que no final chama somente os nomes de cada um dos alunos
'''
    ESSA É A ESTRUTURA
    Alunos |
           L »» Aluno1[(nome), (notas[ notas individuais ]) ]

    Para conseguir o nome do jorge pela lista por exemplo precisaria de:
        alunos[0] 'que é o primeiro aluno na lista' >> alunos[0][0] 'que retornaria o nome "jorge". '
'''

#Calculando a média dos alunos.
for i in range(len(alunos)):
    print(f"Aluno {alunos[i][0]}")
    print(f"Análise do Aluno: (MÉDIA / RESOLUÇÃO) \n\t{procc.calcMedia(alunos[i][1], alunos[i][0])}\n") # Isso aqui foi alterado para comportar o ranking
    
procc.rankAlunos()