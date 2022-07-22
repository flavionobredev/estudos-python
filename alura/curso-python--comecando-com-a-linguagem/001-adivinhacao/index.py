MAX_ATTEMPS = 3
SECRET_NUMBER = 42

from game import make_attempt

print("\n===================")
print("Bem vindo no jogo de Adivinhação")
print("===================\n")


current_attemp = 0
while(current_attemp < MAX_ATTEMPS):
	current_attemp+=1
	# result = check_if_correct(attemp, SECRET_NUMBER)
	result = make_attempt(SECRET_NUMBER)
	if(result.get('match')):
		print(result.get('message'))
		break
	else:
		print(result.get('message'))
		remaing = MAX_ATTEMPS - current_attemp
		print(f"Você tem mais {remaing} tentativas") if remaing > 0 else None
else:
	print("Tentativas excedidas\nNão desista! Tente novamente.")