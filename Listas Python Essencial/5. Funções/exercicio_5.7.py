def contagem_regressiva(n):
    print(n)
    if n>0:
        return contagem_regressiva(n-1)
    else:
        return "Contagem regressiva Finalizada"

print(contagem_regressiva(10))