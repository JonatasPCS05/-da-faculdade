def soma_quadrados(lista):
    soma = 0
    for i in lista:
        quadrado = i**2
        soma += quadrado
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("O resultado da soma dos quadrados é {}".format(soma_quadrados(lista)))