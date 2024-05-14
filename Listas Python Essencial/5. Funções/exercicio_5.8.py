frase = input("Digite a frase decodificada: ")
nova_frase = []
def decifrar_mensagem(frase,marcador):
    if marcador < len(frase):
        if frase[marcador] == " ":
            nova_frase.append(frase[marcador])    
            return decifrar_mensagem(frase, marcador+1)
        if frase[marcador] == "A":
            nova_frase.append("Z")    
            return decifrar_mensagem(frase, marcador+1)
        if frase[marcador] == "a":
            nova_frase.append("z")    
            return decifrar_mensagem(frase, marcador+1)
        ascii = ord(frase[marcador])
        novo_ascii = ascii -1
        novo_caracter = chr(novo_ascii)
        nova_frase.append(novo_caracter)
        return decifrar_mensagem(frase, marcador+1)
    else:
        return nova_frase

print(''.join(decifrar_mensagem(frase, 0)))