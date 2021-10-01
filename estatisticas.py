from os import listdir


def statistical(dir: str) -> None:
    subfolders = listdir(dir)
    qtd_itens = {}
    total = 0
    print("\n\n")

    for i in subfolders:
        qtd_itens[i] = len(listdir(dir + "/" + i))
        total += qtd_itens[i]

    for i in qtd_itens:
        porcentagem = qtd_itens[i] * 100 / total
        print(f"{i:<40}: \t {porcentagem:>30.2f}% ({qtd_itens[i]} itens)")

    print(f"\n{'Total':<40}:{total:>40}")


if __name__ == '__main__':
    statistical("C:\\Users\\ALEXPC\\Downloads\\geral")