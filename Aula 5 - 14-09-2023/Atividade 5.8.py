matriz = [[], []]

for i in range(1, 6):
    matriz[0].append(int(input(f"digite a idade da {i} pessoa: ")))
    matriz[1].append(float(input(f"digite a altura da {i} pessoa: ")))
print("Idades: {}".format(matriz[0][::-1]))
print("Alturas: {}".format(matriz[1][::-1]))