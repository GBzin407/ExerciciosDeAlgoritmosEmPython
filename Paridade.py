numero = int(input("Digite um número inteiro para verificar a sua paridade: "))

resto = numero % 2

if resto == 0:
    print(f"O número {numero} é Par")
elif resto == 1:
    print(f"O número {numero} é Impar")