import os
import zipfile

os.mkdir("Textos")

for i in range(1,4):

    with open(f"Textos/arquivo{i}.txt", "w") as arquivo:
        arquivo.write("Python Essencial")

with zipfile.ZipFile("Textos.zip", "w") as zip:
    for raiz, subdiretorios, arquivos in os.walk("Textos"):
        for arquivo_encontrado in arquivos:
            zip.write(os.path.join(raiz,arquivo_encontrado))