#Exercício 02 - Crie uma aplicação que solicite ao usuário digitar uma palavra e imprima no console a quantidade de caracteres que a palavra possui.

def cont_caracteres():
    palavra = input("Digite uma palavra: ")
    return len(palavra)

print(cont_caracteres())