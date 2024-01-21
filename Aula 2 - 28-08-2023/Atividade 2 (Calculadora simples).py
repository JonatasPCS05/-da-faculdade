numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
operação = input("Digite qual sera a operação (+,-,*,/): ")

if operação == "+":
    print("O resultado da adição é: {}".format(numero1 + numero2))
elif operação == "-":
    print("O resultado da subtração é: {}".format(numero1 - numero2))
elif operação == "*":
    print("O resultado da multiplicação é: {}".format(numero1 * numero2))
elif operação == "/":
    print("O resultado da divisão é: {}".format(numero1 / numero2))
else:
    exit ()