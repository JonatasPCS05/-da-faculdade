quantidade_notas = int(input("Digite a quantidade de notas para calcular a média: "))
soma = 0
i = 0
divisor = quantidade_notas
notas = float()
while quantidade_notas != 0:
    i = i + 1
    notas = float(input("Digite o valor da nota {}: ".format(i)))
    soma = soma + notas
    quantidade_notas = quantidade_notas - 1
media = soma/divisor
print("A média é: {}".format(media))

