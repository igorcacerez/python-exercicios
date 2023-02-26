import random

def jogar():
    print("==================================")
    print("Jogo de adivinhação")
    print("==================================")

    dificuldade = int(input("Escolha a dificuldade (1-3): "))

    sair = False 
    numero = random.randint(1, (dificuldade * 30))

    while (sair == False):
        chute = input("Adivinhe o número que estou pensando: ")

        acertou = numero == int(chute)

        if(acertou):
            print("Você acertou!")
            break
        else:
            if(numero > int(chute)):
                print("Você errou! O número é maior que o que você digitou.")
            else:
                print("Você errou! O número é menor que o que você digitou.")
                
            sair = input("Deseja sair? (s/n) ") == "s"
            
        
        
    print("Fim do jogo!")


