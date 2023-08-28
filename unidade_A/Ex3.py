#Exercício 03 - Crie uma aplicação que solicite ao usuário digitar o seu nome completo e imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.

def cont_de_a():
    nome = input("Digite seu nome completo para contar as letra 'a': ")
    return f"A letra 'a' aparece {nome.count('a')+nome.count('A')} vezes"

print(cont_de_a())