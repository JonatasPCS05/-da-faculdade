matriz = [[],[],[],[]]
media = []
aprovados = 0

for i in range(1,11):
   matriz[0].append(float(input(f"Digite a primeira nota do {i}° aluno: ")))
   matriz[1].append(float(input(f"Digite a segunda nota do {i}° aluno: ")))
   matriz[2].append(float(input(f"Digite a terceira nota do {i}° aluno: ")))
   matriz[3].append(float(input(f"Digite a quarta nota do {i}° aluno: ")))
for i in range(1,11):
    media.append((matriz[0][i-1] + matriz[1][i-1] + matriz[2][i-1] + matriz[3][i-1])/4)
for i in media:
    if i >=7:
        aprovados += 1
    else:
        continue
print(f"O número de alunos aprovados foi de {aprovados}")