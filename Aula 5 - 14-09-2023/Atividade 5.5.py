numeros = []
par = []
impar = []

for i in range(1,21):
    numeros.append(int(input(f"Digite o {i}° numero: ")))
for i in numeros:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(numeros, "\nPares: ", par, "\nImpares: ", impar)