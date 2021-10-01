import os
import shutil


def slice_diretorio(dir_org: str, dir_tgt: str, qtd_slices: int) -> None:
    # list all files in dir
    files = [f for f in os.listdir(dir_org)]
    qtd_files_por_slice = len(files)//qtd_slices

    for i in range(qtd_slices):
        os.mkdir(dir_tgt + "/" + str(i+1))

        for redacao in files[qtd_files_por_slice*i:qtd_files_por_slice*(i+1)]:
            shutil.copyfile(dir_org + "/" + redacao, dir_tgt + "/" + str(i+1) + "/" + redacao)
            os.remove(dir_org + "/" + redacao)

        if i == qtd_slices - 1 and len(files) - qtd_files_por_slice*(i+1) > 0:
            for redacao in files[qtd_files_por_slice * (i + 1):]:
                shutil.copyfile(dir_org + "/" + redacao, dir_tgt + "/" + str(i+1) + "/" + redacao)
                os.remove(dir_org + "/" + redacao)


if __name__ == '__main__':
    diretorio_original = "/Users/alexecheverria/Downloads/Redacoes2"
    diretorio_target = "/Users/alexecheverria/Downloads/Redacoes2"
    slice_diretorio(diretorio_original, diretorio_target, 5)