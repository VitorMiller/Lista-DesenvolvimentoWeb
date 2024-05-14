def importar(modulo):
    try:
        __import__(modulo)
        print("Importado com sucesso")
    except ModuleNotFoundError:
        print("Módulo não encontrado")
    finally:
        print("Operação Finalizada")


importar("vitor")