capital = float(input("Digite quanto é o capitl inicial: "))
juros = float(input("Digite qual é o valor da taxa de juros anual (em decimal): "))
tempo = float(input("Digite o tempo desse investimento (em anos): "))
montante = capital * (1 + juros) ** tempo
print("O montante será: {:.2f}".format(montante))