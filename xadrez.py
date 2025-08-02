def imptabuleiro():
    print("\nBoard\n")
    for linha in tabuleiro:
        print(" ".join(linha))

def posicao(pos):
    colunas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    coluna = colunas[pos[0].lower()]
    linha = 8 - int(pos[1])
    return(linha, coluna)

tabuleiro = [
    ["T", "C", "B", "Q", "R", "B", "C","T"],
    ["P"] *8,
    ["."] *8,
    ["."] *8,
    ["."] *8,
    ["."] *8,
    ["p"] *8,
    ["t", "c", "b", "q", "r", "b", "c","t"]
]

while True:
    imptabuleiro()

    moverpeca = input("Choose a piece and it destiny (Ex.: e2 e4) or 'exit' to leave:")
    if moverpeca.lower() == "exit":
        print("End game...")
        break

    try:
        origem, destino = moverpeca.split(" ")
        origem = posicao(origem)
        destino = posicao(destino)

        peca = tabuleiro[origem[0]][origem[1]]
        if peca == ".":
            print("\nNot has a piece in this position. Please, try again (Ex.: e2 e4):")
            continue
        
        linhaorigem, colunaorigem = origem
        linhadestino, colunadestino = destino

        if peca == "p":
            if colunaorigem == colunadestino:
                if linhaorigem == 6 and linhadestino == 4 and tabuleiro[5][colunaorigem] == "." and tabuleiro[4][colunaorigem] == ".":
                    pass
                elif linhadestino == linhaorigem - 1 and tabuleiro[linhadestino][colunadestino] == ".":
                    pass
                else:
                    print("Invalid movement!")
                    continue
        elif abs(colunaorigem - colunadestino) == 1 and linhaorigem == linhadestino - 1:
            alvo = tabuleiro[linhadestino][colunadestino]
            if alvo.isupper():
                pass
            else:
                print("Stop trying kill your friends.")
                continue
        else:
            print("Invalid movement!")

        if peca == "P":
            if colunaorigem == colunadestino:
                if linhaorigem == 1 and linhadestino == 3 and tabuleiro[2][colunaorigem] == "." and tabuleiro[3][colunaorigem] == ".":
                    pass
                elif linhadestino == linhaorigem + 1 and tabuleiro[linhadestino][colunadestino] == ".":
                    pass
                else:
                    print("Invalid movement!")
                    continue
            elif abs(colunaorigem - colunadestino) == 1 and linhaorigem == linhadestino + 1:
                alvo = tabuleiro[linhadestino][colunadestino]
                if alvo.islower():
                    pass
                else:
                    print("Stop trying kill your friends.")
                    continue
        else:
            print("Invalid movement.")

        tabuleiro[destino[0]][destino[1]] = peca
        tabuleiro[origem[0]][origem[1]] = "."
        

    except Exception as e:
        print("Invalid! Try again. Error: ", e)

