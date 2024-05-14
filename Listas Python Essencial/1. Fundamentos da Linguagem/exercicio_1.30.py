conjunto_a={1,2,3,4,5}
conjunto_b={1,2,3,6,7}

uniao = (conjunto_a | conjunto_b)
intersecao = (conjunto_a & conjunto_b)
diferenca = (conjunto_a - conjunto_b)

print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença: {diferenca}")