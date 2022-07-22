def __check_if_correct(number: int, correct_number: int) -> bool:
	if(number == correct_number):
		return True
	return False


def make_attempt(correct_number: int):
  attempt = input("\nDigite o seu número: ")

  if(not attempt.isdecimal()):
    return {'match': False, 'message': "Por favor, digite um número válido."}

  result = __check_if_correct(int(attempt), correct_number)

  if(result):
    return {'match': True, 'message': "Você acertou! O número correto é {} :)".format(attempt)}

  isLessThan = int(attempt) < correct_number
  return {'match': False, 'message': "Quase! Você digitou um número menor." if isLessThan else "Opa! Você digitou um número maior."}

  # result = check_if_correct(attempt, SECRET_NUMBER)
  # elif(current_attempt < MAX_ATTEMPS):
  #   print(f"Você tem mais {MAX_ATTEMPS - current_attempt} tentativas")
