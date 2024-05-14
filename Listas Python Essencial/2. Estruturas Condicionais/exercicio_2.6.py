palavra = input("Digite uma Palavra: ")

if palavra == palavra[::-1]:
    print("Palíndromo")
else:
    print("Não é Palíndromo")