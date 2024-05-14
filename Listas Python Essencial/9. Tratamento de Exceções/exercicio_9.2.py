def media (lista):
    try:
        return sum(lista)/len(lista)
    except ZeroDivisionError:
        print("Não pode ser vazia a lista")
    except TypeError:
        print("Todos os elementos devem ser números")


lista=[1,2,3]

print(media(lista))