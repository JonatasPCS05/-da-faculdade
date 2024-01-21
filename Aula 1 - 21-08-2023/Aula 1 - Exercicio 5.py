numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
verificador = numero1 - numero2
if verificador == 0:
    print("Os números são iguais!")
elif verificador >= 0:
    print("O {} é maior!".format(numero1))
else:
    print("O {} é maior!".format(numero2))