# Elabore um algoritmo que leia as variáveis C e N respectivamente código e número de horas trabalhadas de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule o excesso e pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.

codigo = int(input("Digite o código: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))

valorHoraNormal = 10.00
valorHoraExcedente = 20.00
limiteHoras = 50

if horas > limiteHoras:
    horasExcedentes = horas - limiteHoras
    salarioExcedente = horasExcedentes * valorHoraExcedente
    salarioTotal = (limiteHoras * valorHoraNormal) + salarioExcedente
else:
    horasExcedentes = 0
    salarioExcedente = 0
    salarioTotal = horas * valorHoraNormal

print(f"Salário toal: R$ {salarioTotal:.2f}")
print(f"Salário excedente: R$ {salarioExcedente:.2f}")