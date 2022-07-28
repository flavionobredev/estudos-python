import curso_python__avancando_na_linguagem.index as forca

print(forca)

def choose():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.play()
    elif(jogo == 2):
        print("Jogando adivinhação")
        curso_python__comecando_com_a_linguagem.adivinhacao.play()

if(__name__ == "__main__"):
    choose()

