emocao = input("Como você está se sentindo agora?")


match emocao.upper():
    case "FELIZ":
        print(":)")
    case "TRISTE":
        print(":(")
