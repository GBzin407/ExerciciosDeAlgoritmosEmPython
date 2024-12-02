numeros = []
quantidade = int(input("Digite a quantidade de nímeros aqui: "))

for i in range(quantidade):
    numero = float(input(f"Digite o valor de número {i + 1} aqui:"))
    numeros.append(numero)

media = sum(numeros) / quantidade

print(f"A média dos {quantidade} números é {media:.2f}")