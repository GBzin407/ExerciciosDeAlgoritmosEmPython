# João papo-de-pescador, homem de bem, comprou um microprocessador para controlar o rendimento diário do seu trabalho, Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estão de São Paulo (50 quilos) deve pagar um amulta de R$ 4,00 por quilo excedente, João precisa que você faça um algoritmo que leia a variável P (peso de peixes) e verifique se há excesso. Se houver, gravar na variável E (excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO. 

p = float(input("Digite o peso em kg:"))

if p > 50:
    e = p - 50
    m = 50 * 4.00
    print(f"Excesso: {e:.2f}kg")
    print(f"Multa: R${m:.2f}")
else:
    print("Excesso: 0 kg")
    print(f"Multa: R$ 0.00")