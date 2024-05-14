import re
frase = input("Digite uma frase: ")
palavras = frase.split()

palavras_trocadas = [ re.sub ("o","a", palavra) for palavra in palavras if re.findall("o", palavra)]

print(palavras_trocadas)