lista1 = [1,2,3]
lista2 = ["Chave1","Chave2","Chave3"]

dicionario = {lista2[i]:lista1[i] for i in range(len(lista1)) }
print(dicionario)