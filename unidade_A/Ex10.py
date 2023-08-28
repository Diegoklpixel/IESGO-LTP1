#Exercício 10 - Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def quant_de_carac(texto):
    contador = texto.lower().replace(' ', '')
    return len(contador)
 
    
print("Esse texto possui ",quant_de_carac(input("Digite texto ")), " caracteres ")
