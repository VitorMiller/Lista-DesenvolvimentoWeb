n = int(input("Digite um número: "))


for i in range (n+1):
    print(f"Fatorial de {i}: ")
    fatorial = 1
    for j in range (i):
        fatorial = fatorial * (j+1)
    print(fatorial)
