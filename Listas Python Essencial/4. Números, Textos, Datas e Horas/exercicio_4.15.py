import re
frase = input("Digite uma frase: ")

palavras=frase.split()
print(palavras)

for palavra in palavras:
    repeticoes = palavras.count(palavra)
    print(f"A palavra {palavra}, ocorre {repeticoes} vezes")