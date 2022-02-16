lista = []

with open("/Users/alexecheverria/Downloads/tabela.txt") as gaymer:
    for linha in gaymer:
        try:
            lista.append(int(linha[:-3]))

        except Exception as e:
            print(e)

for i in lista:
    print(i)