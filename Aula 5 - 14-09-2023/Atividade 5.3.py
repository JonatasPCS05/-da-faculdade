notas = []

for i in range(1,5):
    notas.append(float(input(f"Digite a nota {i}: ")))
print("As notas foram: {}\nA média foi: {}".format(notas, sum(notas)/4))