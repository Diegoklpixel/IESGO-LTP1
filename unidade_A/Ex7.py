#Exercício 07 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas. Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.
def formatação_de_nome(nome):
    pa_nomes = nome.split( )
    nome_usuario = pa_nomes[0]
    sobrenome_usuario =" ".join(pa_nomes[1:])
    nome_completo = nome.upper()
    todo_nome = len(nome)

     
    print("Nome: "+nome_completo.lower())
    print("tem ",todo_nome, " caracteres ")

formatação_de_nome(input("Digite seu nome completo "))
