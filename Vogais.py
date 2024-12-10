def conta_vogais(texto):
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    contador = 0

    for char in texto:
        if char in vogais:  
            contador += 1 
    
    return contador

texto = input("Digite uma string: ")

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")