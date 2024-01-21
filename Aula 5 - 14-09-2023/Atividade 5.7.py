def multiplicação(lista):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado

lista = []

for i in range(1,6):
    lista.append(int(input(f"Digite o {i}° número: ")))
print(lista)
print("O resultado da soma é: {}".format(sum(lista)))
print("O resultado da multiplicação é: {}".format(multiplicação(lista)))