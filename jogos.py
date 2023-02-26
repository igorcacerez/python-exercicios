import forca
import adivinha

print("==================================")
print("Escolha o seu Jogo.")
print("==================================")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    adivinha.jogar()
else:
    print("Jogo não encontrado!")
