import json
import random

def jogar():
    jogar = True
    
    while (jogar):
        jogo()
        jogar = input("Deseja jogar novamente? (S/N) ").upper() == "S"

def jogo(): 
    print("==================================")
    print("Jogo de Forca")
    print("==================================")
    
    conteudo = json.load(open("palavras.json"))
    
    palavra_secreta = conteudo["palavras"][random.randrange(0, len(conteudo["palavras"]))].upper()
    palavra = ["_" for letra in palavra_secreta]
    letrasErradas = []
    vida = 5

    print("A palavra secreta é: {}".format(palavra))
    print("\n \n")
    
    while(True):
        
        if (vida <= 0):
            print("Você perdeu!")
            break
            
        if ("_" not in palavra):
            print("Você ganhou!")
            break
        
        acertou = False
        
        print("Você tem {} chances".format(vida))
        chute = input("Qual letra? ").upper()
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                palavra[index] = letra
                acertou = True
            index += 1
        
        if(not acertou):
            letrasErradas.append(chute)
            vida -= 1 
            
        print("\n")     
        print("Letras erradas: {}".format(letrasErradas))
        print("A palavra secreta é: {}".format(palavra))
        print("\n \n")  
    
if(__name__ == "__main__"):
    jogar()