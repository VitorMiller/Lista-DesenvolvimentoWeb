import re
cpf = input("Digite um cpf válido: ")

if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
    print("válido")
else:
    print("Inválido")