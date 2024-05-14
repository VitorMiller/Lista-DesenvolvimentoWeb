def acertar_palavra(palavra_chave):
    try:
        while True:
            palavra_palpite = input("Adivinhe a palavra: ")
            if not palavra_palpite.isalpha():
                raise ValueError("A palavra deve somente possuir letras")
            if palavra_palpite == palavra_chave:
                print("Você acertou!")
                break
    
    except ValueError as e:
        print(e)
            
acertar_palavra("Vitor")