# – Em uma loja e CD´s existem apenas quatro tipos de preços que estão associados a cores. Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. Desenvolva o algoritmo que a partir a entrada da cor o software mostre o preço. A loja está atualmente com a seguinte tabela de preços. 

c = int(input('''-ESCOLHA UMA COR-
              1. Verde
              2. Azul
              3. Amarelo
              4. Vermelho
              Digite um número aqui: '''))

if c == 1:
    print("O preço do CD será de 10 reais")
elif c == 2:
    print("O preço do CD será de 20 reais")
elif c == 3:
    print("O preço do CD será de 30 reais")
elif c == 4:
    print("O preço do CD será de 40 reais")
elif c > 4 or c < 1:
    print("Erro!")