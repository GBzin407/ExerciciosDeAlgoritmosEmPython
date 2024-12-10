def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
    
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")