#Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplucação que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def sub_vogais():
    palavra = input("Digite uma palavra: ")
    return palavra.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

print(sub_vogais())