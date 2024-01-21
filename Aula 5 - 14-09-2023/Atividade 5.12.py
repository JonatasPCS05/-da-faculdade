matriz = [[11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16], [1.4, 1.4, 1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.6, 1.7, 1.8, 1.9, 1.9, 1.8, 1.7, 1.6, 1.5, 1.5, 1.6, 1.7, 1.8, 1.9, 1.9, 1.8, 1.7, 1.6, 1.5]]

soma = 0
contador = 0

for i in range(30):
    if matriz[0][i] > 13:
        soma += matriz[1][i]
        contador += 1
    else:
        continue

media_altura13 = soma/contador
contador2 = 0

for i in range(30):
    if matriz[0][i] > 13 and matriz[1][i] < media_altura13:
        contador2 += 1
    else:
    	continue
print(f"Tem {contador2} alunos com mais de 13 anos abaixo da média")