print("===================")
print("Bem vindo no jogo de Adivinhação")
print("===================")

secret_number = 42

attemp = int(input("Digite o seu numero: "))

if(attemp == secret_number):
    print("Parabéns, você acertou! O numero secreto é: ", secret_number)
elif(attemp > secret_number):
    print("Quase! Você informou um número maior.")
elif(attemp < secret_number):
    print("Quase! Você informou um número menor.")