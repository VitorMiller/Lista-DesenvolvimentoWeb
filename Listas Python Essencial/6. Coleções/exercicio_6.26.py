def gerar_numeros():
    numero = 1
    while True:
        yield numero
        numero +=1

gerador = gerar_numeros()
for i in range(10):
    print(next(gerador))