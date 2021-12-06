def load_files(directory: str) -> list:
    array = []

    with open(directory) as txt:
        for line in txt:
            list_aux = line.split(",")
            array.append(list_aux)

    array.sort(key=lambda x: x[0])  # selecionando a chave da lista para realizar o sort

    return array


def load_redacoes(directory: str) -> list:
    """ Deve-se colocar as redacoes todas juntas dentro do diretorio que se deseja organizar...
    :rtype: list
    """
    from os import listdir
    redacoes = listdir(directory)

    redacoes.sort()

    return redacoes


def treating_label(label: str) -> str:
    aux = ""
    for char in label:
        if char not in ['"', '[', ']', '/']:
            aux += char

    if "\n" in aux:
        return aux[:-1]

    else:
        return aux


def realoc_redacoes(dir_redacoes: str, dir_csv: str) -> None:
    """ Dir_redacoes é o diretório da pasta em que as redacoes estão. É importante que estejam todas elas direto na
     raiz do diretorio, ou seja, sem estar em sub-pastas. """

    import shutil
    from os import remove, mkdir

    redacoes_anotadas = load_files(dir_csv)
    redacoes_avulsas = load_redacoes(dir_redacoes)
    for anotacao in redacoes_anotadas:
        redacao = anotacao[0]
        rotulo = treating_label(anotacao[1])

        for nome_red in redacoes_avulsas:
            if redacao == nome_red and "," not in rotulo:
                try:
                    # se for windows, trocar a / por \\
                    shutil.copyfile(dir_redacoes + f"/{redacao}", dir_redacoes + f"/{rotulo}/{redacao}")
                    remove(dir_redacoes + f"/{redacao}")

                except:
                    mkdir(dir_redacoes + f"/{rotulo}")
                    shutil.copyfile(dir_redacoes + f"/{redacao}", dir_redacoes + f"/{rotulo}/{redacao}")
                    remove(dir_redacoes + f"/{redacao}")
                break


if __name__ == '__main__':
    realoc_redacoes("/Users/alexecheverria/Downloads/luizf", "arquivos/luisf.csv")