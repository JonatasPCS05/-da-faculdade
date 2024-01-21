lista = []
consoante = []
contador = 0

for i in range(1,11):
    lista.append(input(f"Digite a {i}º letra: "))
for i in lista:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    else:
        consoante.append(i)
        contador +=1
print("Nessa lista tem {} consoantes, que são: {}".format(contador, consoante))