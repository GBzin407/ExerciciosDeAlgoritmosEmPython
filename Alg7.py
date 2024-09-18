# A secretária de Meio Ambiente que controla o índice de poluição mantém 3 grupos que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritmo que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas. 

ip = float("Digite o índice: ")

if ip >= 0.5:
    print("Todos os grupos, suspendam as atividades.")
elif ip >= 0.4:
    print("Primeiro e segundo grupo, suspendam as atividades.")
elif ip >= 0.3:
    print("Primeiro grupo, suspendam as atividades.")
else:
    print("Índice bom.")