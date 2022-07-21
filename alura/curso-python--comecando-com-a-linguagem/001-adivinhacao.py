print("===================")
print("Bem vindo no jogo de Adivinhação")
print("===================")

secret_number = 42

attemp = int(input("Digite o seu numero: "))

if(attemp == secret_number):
    print("Parabéns, você acertou!")
else:
    print("Você errou, o número secreto era {}".format(secret_number))