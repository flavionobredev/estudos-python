def make_attempt(correct_number: int):
  attempt = input("\nDigite o seu número: ")

  if(not attempt.isdecimal()):
    return {'match': False, 'message': "Por favor, digite um número válido."}

  result = int(attempt) == correct_number

  if(result):
    return {'match': True, 'message': "Você acertou! O número correto é {} :)".format(attempt)}

  isLessThan = int(attempt) < correct_number
  return {'match': False, 'message': "Quase! Você digitou um número menor." if isLessThan else "Opa! Você digitou um número maior."}
