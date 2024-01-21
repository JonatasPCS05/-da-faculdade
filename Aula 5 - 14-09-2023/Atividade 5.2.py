lista = []

for i in range(1,11):
    lista.append(float(input(f"Digite o {i}º número: ")))
print(lista[::-1])