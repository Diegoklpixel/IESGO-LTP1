#Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def apagar():
    vogal = input("Digite um texto: ")
    return vogal.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")

print(apagar())