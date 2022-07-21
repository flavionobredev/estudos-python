MAX_ATTEMPS = 3
SECRET_NUMBER = 42

def check_if_correct(number: int, correct_number: int) -> bool:
	if(number == correct_number):
		print("Parabéns, você acertou! O numero secreto é: ", correct_number)
		return True
	elif(number > correct_number):
		print("Quase! Você informou um número maior.")
	elif(number < correct_number):
		print("Quase! Você informou um número menor.")
	
	return False


print("\n===================")
print("Bem vindo no jogo de Adivinhação")
print("===================\n")


current_attemp = 0
while(current_attemp < MAX_ATTEMPS):
	attemp = int(input("\nDigite o seu numero: "))
	current_attemp+=1
	result = check_if_correct(attemp, SECRET_NUMBER)
	if(result):
		break
	elif(current_attemp < MAX_ATTEMPS):
		print(f"Você tem mais {MAX_ATTEMPS - current_attemp} tentativas")
else:
	print("Tentativas excedidas\nNão desista! Tente novamente.")