import random
import re
nome = input("Digite seu nome: ")
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

contador = 0
acertos = 0
letras_nome = list(nome)

while acertos != len(nome): 
    contador += 1
    print(contador)
    letra_aleatoria = random.choice(letras)
    print(letra_aleatoria)
    if letra_aleatoria in letras_nome:
        acertos += 1
        letras_nome.remove(letra_aleatoria)

print(contador)


