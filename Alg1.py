# Em uma escola, a média final é dada pela média aritmética de três notas. E a mesma tem o seguinte esquema de avaliação:
# 0 - 4.9 = Aluno em recuperação
# 5 - 6.9 = Aluno em prova final
# 7 - 10 = Aluno passado por média
# Desenvolva um algoritmo que a partir da entrada das três notas mostre a situação do aluno. No caso do aluno em recuperação e prova final, mostre também quanto o aluno irá precisar para passar. No caso da recuperação a nota necessária para passar é dada por 10 – Média + 2 e na prova final é dado por 10 – Média. 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

m = (n1 + n2 + n3) / 3

if m < 5:
    r = 10 - m + 2
    print(f'''-RECUPERAÇÃO-
O aluno precisa de {r:.2f} para passar de ano.''')
elif 5 <= m < 7:
    r = 10 - m
    print(f'''-PROVA FINAL-
O aluno precisa de {r:.2f} para passar de ano.''')
else:
    print("O aluno passou de ano.")
