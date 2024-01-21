def intercalar_vetores(vetor1, vetor2, vetor3):
    vetor4 = []
    for i in range(len(vetor1)):
        vetor4.append(vetor1[i])
        vetor4.append(vetor2[i])
        vetor4.append(vetor3[i])
    return vetor4

vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
vetor4 = intercalar_vetores(vetor1, vetor2, vetor3)

print("Vetor 1: {}".format(vetor1))
print("Vetor 2: {}".format(vetor2))
print("Vetor 3: {}".format(vetor3))
print("Vetor 1 e 2 e 3 intercalados: {}".format(vetor4))