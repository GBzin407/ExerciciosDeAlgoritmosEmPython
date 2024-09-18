#Desenvolva um algoritmo capaz e encontrar o menor dentre 3 números inteiros quaisquer dados pelo teclado. 

a = int(input("Escreva um número:"))
b = int(input("Escreva um número:"))
c = int(input("Escreva um número:"))

if a <= b and a <= c:
    print("menor = A")
elif b <= a and b <= c:
    print("Menor = B")
else:
    print("Menor = C")