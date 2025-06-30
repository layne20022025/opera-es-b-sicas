import tkinter as tk
from tkinter import messagebox
import random

spider_emojis = ["🕷️", "🕸️", "🕷️", "🕸️"]
frases_spidey = [
    "Com grandes poderes vêm grandes responsabilidades... e grandes resultados!",
    "O Homem-Aranha nunca erra uma conta!",
    "Sentido aranha diz: esse resultado está incrível!",
    "Mais rápido que uma teia!"
]

# Função de cálculo e exibição
def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        resultados = [
            ("Soma", a + b, f"{a} + {b} = {a + b}"),
            ("Subtração", a - b, f"{a} - {b} = {a - b}"),
            ("Multiplicação", a * b, f"{a} x {b} = {a * b}"),
            ("Divisão", a / b if b != 0 else 'Indefinido', f"{a} ÷ {b} = {a / b if b != 0 else 'Indefinido'}")
        ]
        texto = ""
        for i, (nome, resultado, expressao) in enumerate(resultados):
            texto += f"{spider_emojis[i]} {nome}: {expressao}\n{random.choice(frases_spidey)}\n\n"
        resultado_label.config(text=texto)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite números válidos!")

# Janela principal
root = tk.Tk()
root.title("Calculadora do Homem-Aranha 🕷️🕸️")
root.geometry("420x400")
root.configure(bg="#e0e7ef")

# Título
titulo = tk.Label(root, text="Calculadora do Homem-Aranha 🕷️🕸️", font=("Arial", 16, "bold"), bg="#e0e7ef", fg="#c0392b")
titulo.pack(pady=10)

# Instrução
instrucao = tk.Label(root, text="Digite dois números para ver os poderes matemáticos do Spidey!", font=("Arial", 11), bg="#e0e7ef")
instrucao.pack(pady=5)

# Entradas
frame_inputs = tk.Frame(root, bg="#e0e7ef")
frame_inputs.pack(pady=10)

label1 = tk.Label(frame_inputs, text="Primeiro número:", font=("Arial", 11), bg="#e0e7ef")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame_inputs, font=("Arial", 11), width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame_inputs, text="Segundo número:", font=("Arial", 11), bg="#e0e7ef")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame_inputs, font=("Arial", 11), width=10)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Botão de calcular
calcular_btn = tk.Button(root, text="Lançar teia e calcular! 🕸️", font=("Arial", 12, "bold"), bg="#c0392b", fg="white", command=calcular)
calcular_btn.pack(pady=15)

# Resultado
resultado_label = tk.Label(root, text="", font=("Arial", 11), bg="#e0e7ef", justify="left")
resultado_label.pack(pady=10)

# Rodapé
rodape = tk.Label(root, text="Com grandes poderes matemáticos, vêm grandes diversões!", font=("Arial", 9, "italic"), bg="#e0e7ef", fg="#888")
rodape.pack(side="bottom", pady=8)

root.mainloop() 