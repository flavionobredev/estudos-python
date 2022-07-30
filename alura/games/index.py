import os
import sys
# deve usar o caminho absoluto do modulo. no caso, a execução desse script deve ser feita na pasta onde ele está.  TODO: pegar caminho absoluto correto, independente do local de execução do script
sys.path.append(os.path.abspath("curso_python__comecando_com_a_linguagem"))

import curso_python__comecando_com_a_linguagem.index as adivinhacao
import curso_python__avancando_na_linguagem.index as forca

# print(sys.path)

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
    adivinhacao.play()


if(__name__ == "__main__"):
  choose()
