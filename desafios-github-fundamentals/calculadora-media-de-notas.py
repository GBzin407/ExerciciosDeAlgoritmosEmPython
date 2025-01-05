notas = [float(input(f"Digite a nota {i + 1}: ")) for i in range(3)]
media = sum(notas) / len(notas)

print(f"A média das notas é: {media:.2f}")