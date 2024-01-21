n = int(input("Digite a quantidade de alunos: "))
matriz = [[],[],[],[]]

for i in range(1,n+1):
    matriz[0].insert(i, input(f"Digite o nome do aluno {i}: "))
    matriz[1].insert(i, float(input(f"Digite a nota do aluno {matriz[0][i-1]}: ")))
    matriz[2].insert(i, float(input(f"Digite a frenquencia do aluno {matriz[0][i-1]}: ")))
    if matriz[2][i-1] < 75:
        matriz[3].insert(i, "Reprovado")
    elif matriz[1][i-1] < 7:
        matriz[3].insert(i, "Reprovado")
    else:
        matriz[3].insert(i, "Aprovado")
for i in range(1,n+1):
    print("O aluno {} está {}".format(matriz[0][i-1], matriz[3][i-1]))