from constants import INITIAL_POINTS, SECRET_NUMBER, MAX_ATTEMPS
from game import make_attempt


def play():
  print("\n===================")
  print("Bem vindo no jogo de Adivinhação")
  print("===================\n")

  current_attemp = 0
  points = INITIAL_POINTS
  for current_attempt in range(0, MAX_ATTEMPS):
    current_attemp += 1
    result = make_attempt(SECRET_NUMBER)
    if(result.get('match')):
      print(result.get('message'))
      print("Conseguiu acertar a resposta na {}ª tentativa".format(current_attemp))
      print("Pontos: ", points)
      break
    else:
      print(result.get('message'))
      remaing = MAX_ATTEMPS - current_attemp
      points -= int(INITIAL_POINTS/MAX_ATTEMPS)
      print(f"Você tem mais {remaing} tentativas") if remaing > 0 else None
  else:
    print("Tentativas excedidas\nNão desista! Tente novamente.")


if(__name__ == "__main__"):
  play()
