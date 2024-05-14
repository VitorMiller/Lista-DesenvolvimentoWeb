import math

angulo = int(input("Digite um ângulo entre 0 e 360 graus para que seja calculado o seno, cosseno e tangente: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"O ângulo de {angulo} graus possui os seguintes valores de seno, cosseno e tangente: ")
print(f"Seno: {seno} ")
print(f"Cosseno: {cosseno} ")
print(f"Tangente: {tangente} ")
