import os
import shutil


def copia_redacoes(dir_orig: str, dir_tgt: str, dir_lista_red: str, nome_pasta: str = "redacoes") -> None:
    # list all files in dir
    diretorio = f"{dir_tgt}/{nome_pasta}"
    lista_red = []

    try:
        os.mkdir(diretorio)
    except Exception as e:
        print("Exceção:", e)

    with open(dir_lista_red, "r", encoding='utf-8-sig') as nome_red:
        for linha in nome_red:
            if "\n" in linha:
                lista_red.append(linha[:-1])
            else:
                lista_red.append(linha)

    for red in lista_red:
        shutil.copyfile(f"{dir_orig}/{red}", f"{dir_tgt}/{nome_pasta}/{red}")


if __name__ == '__main__':
    diretorio_original = "/Users/alexecheverria/Downloads/5"
    diretorio_target = "/Users/alexecheverria/Downloads"
    dir_nome_redacoes = "/Users/alexecheverria/Downloads/LUIZG.txt"
    nome_pasta = "luizgbranco"
    # Diretorio das redações + dir destino + qtd de redações por pasta + qtd de pastas + qtd de subdivisoes das pastas
    copia_redacoes(diretorio_original, diretorio_target, dir_nome_redacoes, nome_pasta)
