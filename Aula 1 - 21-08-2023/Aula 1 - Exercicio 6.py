numero1 = float(input("Digite o primeiro numéro: "))
numero2 = float(input("Digite o segundo numéro: "))
numero3 = float(input("Digite o terceiro numéro: "))
if numero1<numero2 and numero1<numero3:
    print("O {} é o menor!".format(numero1))
elif numero2<numero1 and numero2<numero3:
    print("O {} é o menor!".format(numero2))
else:
    print("O {} é o menor!".format(numero3))