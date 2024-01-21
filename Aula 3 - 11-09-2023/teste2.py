import os
n = int(input("Digite a quantidade de alunos: "))
medias = []
for i in range(n):
    medias.append(float(input("entre com a média: ")))
os.system("cls")
print(medias)