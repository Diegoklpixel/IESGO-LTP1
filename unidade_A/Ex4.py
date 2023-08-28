#Exercício 04 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console o nome com todas as letras maiúsculas.

def maiuscola():
    mais = input("Digite seu nome completo: ")
    return mais.swapcase()

print(maiuscola())