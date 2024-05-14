import datetime
agora = datetime.datetime.now()
inicio_ano = datetime.datetime(2024,1,1)
diferenca = agora-inicio_ano
print(agora)
print(inicio_ano)
print(f"Já se passaram {int((diferenca.days)/7)} semanas")

