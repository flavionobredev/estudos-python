# python não faz conversão implícita de tipos de dados.
# Exemplo:
a = 10
b = "10"
print(a * b) # o resultado será a string "10" repetida 10 vezes (10 * "10")

# python não faz concatenação de strings com numeros.
# Exemplo:
a = "10"
b = 10
print(a + b) # será gerado um erro de compilação