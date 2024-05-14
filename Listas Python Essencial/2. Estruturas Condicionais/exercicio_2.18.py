numeros = []
impares = 0
for numero in range(5):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

for numero in numeros:
    if not (numero % 2 == 0):
        impares += 1

if impares > 0:
    print("Ao menos um dos números é ímpar!")
else:
    print("Todos são pares!")