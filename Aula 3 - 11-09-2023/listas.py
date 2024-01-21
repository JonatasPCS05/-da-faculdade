lista = []
lista1 = [1, 2, 3]
lista2 = ['nome', 'nota']

lista1.append(1)
print(len(lista1))
print(lista1[-1])
print(min(lista1))
print(max(lista1))

print(len(lista2))
print(min(lista2))
lista2.append("bola")
lista2.append("aula")
print(len(lista2))
print(min(lista2))
lista2.append("aul")
lista2.append("ceu")
lista2.append("tu")
print(len(lista2))
print(min(lista2))
print(lista2)

lista2.append("media")
if "media" in lista2:
    print(lista2)
    print("Tá sim")

lista2[1] = 'texto'
print(lista2)

lista2.insert(1, "nome")
print(lista2)

lista2.remove("tu")
print(lista2)

lista2.pop()
print(lista2)

#del(lista2)
print(lista2)

print(lista1)
lista1.clear()
print(lista1)