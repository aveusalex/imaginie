import numpy as np
import os
import shutil
from dividirEmClusters import slice_diretorio


def separa_redacoes(dir_orig: str, dir_tgt: str, qtd_red: int, divisoes: int = 1, qtd_slices: int = 2) -> None:
    # list all files in dir
    files = [f for f in os.listdir(dir_orig)]

    for i in range(divisoes):
        diretorio = f"{dir_tgt}/Redacoes{i+1}"
        try:
            os.mkdir(diretorio)
        except:
            pass

        random_files = np.random.choice(files, qtd_red, replace=False)
        for elemento in random_files:
            files.remove(elemento)

        for redacao in random_files:
            shutil.copyfile(f"{dir_orig}/{redacao}", f"{dir_tgt}/Redacoes{i + 1}/{redacao}")

        slice_diretorio(diretorio, diretorio, qtd_slices)


if __name__ == '__main__':
    diretorio_original = "/Users/alexecheverria/Downloads/essays"
    diretorio_target = "/Users/alexecheverria/Downloads"
    # Diretorio das redações + dir destino + qtd de redações por pasta + qtd de pastas + qtd de subdivisoes das pastas
    separa_redacoes(diretorio_original, diretorio_target, 20000, 5, 10)
