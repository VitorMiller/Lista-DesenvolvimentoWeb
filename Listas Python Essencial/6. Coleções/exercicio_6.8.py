numeros = input("Digite a sequencia de números separados por espaço: ")
numeros_separados =[]

for numero in numeros.split():
    if numero == " ":
        pass
    else:
        numeros_separados.append(int(numero))

quadrados = list(map(lambda x: x**2, numeros_separados))
print(quadrados)