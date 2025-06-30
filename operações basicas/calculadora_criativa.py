import time
import random

# Função para imprimir com efeito de teia (digitação)
def teia(texto, delay=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

spider_emojis = ["🕷️", "🕸️", "🕷️", "🕸️"]
frases_spidey = [
    "Com grandes poderes vêm grandes responsabilidades... e grandes resultados!",
    "O Homem-Aranha nunca erra uma conta!",
    "Sentido aranha diz: esse resultado está incrível!",
    "Mais rápido que uma teia!"
]

teia("Bem-vindo à Calculadora do Homem-Aranha! 🕷️🕸️\n")
teia("Prepare-se para resultados espetaculares!\n")

a = float(input("Digite o primeiro número (com poder e responsabilidade): "))
b = float(input("Digite o segundo número (com agilidade): "))

operacoes = [
    ("Soma", a + b, f"{a} + {b} = {a + b}"),
    ("Subtração", a - b, f"{a} - {b} = {a - b}"),
    ("Multiplicação", a * b, f"{a} x {b} = {a * b}"),
    ("Divisão", a / b if b != 0 else 'Indefinido', f"{a} ÷ {b} = {a / b if b != 0 else 'Indefinido'}")
]

teia("Lançando teias matemáticas...\n", 0.05)
for i, (nome, resultado, expressao) in enumerate(operacoes):
    teia(f"{spider_emojis[i]} {nome}: {expressao}")
    teia(random.choice(frases_spidey))
    time.sleep(0.5)

teia("\nObrigado por usar a Calculadora do Homem-Aranha! Com grandes poderes matemáticos, vêm grandes diversões! 🕷️🕸️") 