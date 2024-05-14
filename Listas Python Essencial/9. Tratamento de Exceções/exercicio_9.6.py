import random

class RangeErrado(Exception):
    def __init__(self):
        super().__init__("Deve ser entre 1 e 10")



sorteado = random.randint(1,10)



while True:
    try:
        palpite = int (input("DIgite um número entre 1 e 10: "))
        if palpite < 1 or palpite>10:
            raise RangeErrado()

        if palpite == sorteado:
            print("Você acertou!!")
            break
        else:
            print("Errou, tente novamente")
    except RangeErrado as e:
        print(e)    
    except ValueError:
        print("Deve ser um número")
            
