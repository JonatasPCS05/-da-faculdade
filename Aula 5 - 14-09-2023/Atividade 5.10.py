def intercalar_vetores(vetor1, vetor2):
    vetor3 = []
    for i in range(len(vetor1)):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])
    return vetor3

vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor3 = intercalar_vetores(vetor1, vetor2)

print("Vetor 1: {}".format(vetor1))
print("Vetor 2: {}".format(vetor2))
print("Vetor 1 e 2 intercalados: {}".format(vetor3))