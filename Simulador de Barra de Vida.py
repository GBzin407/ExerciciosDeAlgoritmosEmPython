import tkinter as tk

def atualizar_barra():
    global vida_atual, vida_total

    if vida_atual == 0:
        resultado_label.config(text="O jogador morreu! Não é possível alterar a vida.")
        return

    try:
        valor = int(entrada_valor.get())
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido.")
        return

    vida_atual += valor

    if vida_atual > vida_total:
        vida_atual = vida_total
    elif vida_atual < 0:
        vida_atual = 0

    proporcao = vida_atual / vida_total
    barra_vida_canvas.coords(barra_vida_rect, 10, 10, 10 + proporcao * 300, 30)
    vida_atual_label.config(text=f"Vida atual: {vida_atual}/{vida_total}")

    if vida_atual == 0:
        resultado_label.config(text="O jogador morreu!")
    else:
        resultado_label.config(text="")

def iniciar_jogo():
    global vida_total, vida_atual

    try:
        vida_total = int(entrada_vida_total.get())
    except ValueError:
        erro_label.config(text="Por favor, insira um número válido para a vida total.")
        return

    vida_atual = vida_total

    proporcao = vida_atual / vida_total
    barra_vida_canvas.coords(barra_vida_rect, 10, 10, 10 + proporcao * 300, 30)
    vida_atual_label.config(text=f"Vida atual: {vida_atual}/{vida_total}")
    resultado_label.config(text="")

    mostrar_tela_barra()

def mostrar_tela_barra():
    tela_vida.pack_forget()
    tela_barra.pack(fill="both", expand=True)

def mostrar_tela_inicial():
    tela_barra.pack_forget()
    tela_vida.pack(fill="both", expand=True)

def reiniciar_programa():
    global vida_total, vida_atual

    vida_total = 0
    vida_atual = 0

    entrada_vida_total.delete(0, tk.END)
    erro_label.config(text="")

    mostrar_tela_inicial()

root = tk.Tk()
root.title("Simulador de Barra de Vida")
root.geometry("600x400")

vida_total = 0
vida_atual = 0

tela_vida = tk.Frame(root)
tela_barra = tk.Frame(root)

def centralizar_widgets(tela):
    tela.pack_propagate(False)
    tela.grid_rowconfigure(0, weight=1)
    tela.grid_columnconfigure(0, weight=1)

centralizar_widgets(tela_vida)
centralizar_widgets(tela_barra)

conteudo_tela_vida = tk.Frame(tela_vida)
conteudo_tela_vida.grid(row=0, column=0)

vida_total_label = tk.Label(conteudo_tela_vida, text="Digite a quantidade de vida total do jogador:")
vida_total_label.pack(pady=5)

entrada_vida_total = tk.Entry(conteudo_tela_vida)
entrada_vida_total.pack(pady=5)

iniciar_button = tk.Button(conteudo_tela_vida, text="Iniciar Jogo", command=iniciar_jogo)
iniciar_button.pack(pady=10)

erro_label = tk.Label(conteudo_tela_vida, text="", fg="red")
erro_label.pack(pady=10)

conteudo_tela_barra = tk.Frame(tela_barra)
conteudo_tela_barra.grid(row=0, column=0)

barra_vida_canvas = tk.Canvas(conteudo_tela_barra, width=310, height=40, bg="white")
barra_vida_canvas.pack(pady=10)
barra_vida_canvas.create_rectangle(10, 10, 310, 30, outline="black")
barra_vida_rect = barra_vida_canvas.create_rectangle(10, 10, 310, 30, fill="green")

vida_atual_label = tk.Label(conteudo_tela_barra, text="Vida atual: 0/0")
vida_atual_label.pack(pady=5)

valor_label = tk.Label(conteudo_tela_barra, text="Digite o valor de dano (negativo) ou recuperação (positivo):")
valor_label.pack(pady=5)

entrada_valor = tk.Entry(conteudo_tela_barra)
entrada_valor.pack(pady=5)

botoes_frame = tk.Frame(conteudo_tela_barra)
botoes_frame.pack(pady=10)

aplicar_button = tk.Button(botoes_frame, text="Aplicar", command=atualizar_barra)
aplicar_button.pack(side=tk.LEFT, padx=5)

reiniciar_button = tk.Button(botoes_frame, text="Reiniciar", command=reiniciar_programa)
reiniciar_button.pack(side=tk.LEFT, padx=5)

resultado_label = tk.Label(conteudo_tela_barra, text="", fg="red")
resultado_label.pack(pady=10)

mostrar_tela_inicial()

root.mainloop()