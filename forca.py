import random

palavras = ["Africa", "Abner", "Churrasco", "otorrinolaringologista", "pneumoultramicroscopicossilicovulcanoconiótico"]

def jogoDaForca():
    palavraSecreta = random.choice(palavras)
    letrasCertas = ["-"] * len(palavraSecreta)
    letrasErradas = []
    tentativas = len(palavraSecreta)  # Aqui está o número de tentativas, inicialmente igual ao número de letras.
    
    print("Bem-vindo ao jogo da forca!")
    print("A quantidade de tentativas é equivalente ao número de letras na palavra secreta.")
    
    while "-" in letrasCertas and tentativas > 0:
        print(" " . join(letrasCertas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letrasErradas)}")
        
        acao = input("Deseja chutar uma letra (1) ou adivinhar a palavra (2)? ").upper()
        
        if acao == "1":
            chute = input("Chute uma letra: ").lower()
            
            if len(chute) != 1:
                print("Digite apenas uma letra.")
                continue
            
            if chute in letrasErradas or chute in letrasCertas:
                print("Letra já chutada.")
                continue
            
            if chute in palavraSecreta:
                for i, letra in enumerate(palavraSecreta):
                    if letra == chute:
                        letrasCertas[i] = chute
            else:
                letrasErradas.append(chute)
                tentativas -= 1
        elif acao == "2":
            chutePalavra = input("Tente adivinhar a palavra: ").lower()
            
            if chutePalavra == palavraSecreta:
                print("Parabéns! Você ganhou!")
                return
            else:
                print("Palavra incorreta.")
                tentativas -= 1 
        else:
            print("Opção inválida.")
            
    if "-" not in letrasCertas:
        print(" ".join(letrasCertas))
        print("Parabéns! Você ganhou!")
    else:
        print(f"Game over! A palavra era {palavraSecreta}.")
        
jogoDaForca()