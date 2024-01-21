reais = [100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]

valor_compra = float(input("Digite o valor da compra: "))
valor_dado = float(input("Digite o valor pago: "))

if valor_compra > valor_compra:
    print("O valor não é suficiente")
else:
    troco = valor_dado - valor_compra
    print("Troco a ser dado:")
    for reais in reais:
        if troco >= reais:
            quantidade = int(troco // reais)
            print("{} {} de {}".format(quantidade, "nota" if reais > 1 else "moeda", reais))
            troco -= quantidade * reais