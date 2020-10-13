from helper import *

# Escolhendo Palavra
selecionada = selecionaPalavra(carregaPalavras())

escolhida = ['_' if i != ' ' else ' ' for i in selecionada]
space = True if " " in escolhida else False

chutes = []

paraWhile = 0

caixaTexto(f'A palavra possui {len(selecionada) - 1 if space else len(selecionada)} Letras', 30)

while paraWhile != 6:

    caixaTexto(f"{''.join(escolhida)}", 34)

    caixaTexto("Digite uma Letra para a  Palavra", 35)
    letra = input('--> ')
    print('\n' * 10)

    verificaAcerto = 0

    for i in range(len(selecionada)):
        if letra == selecionada[i]:
            escolhida[i] = letra
            verificaAcerto += 1

    chutes.append(letra)
    caixaTexto(f"Letras Usadas: {' '.join(chutes)}", 33)

    if verificaAcerto == 0:
        caixaTexto("A letra não consta nesta palavra", 31)
        paraWhile += 1
        chances(paraWhile)
    else:
        caixaTexto("Parabéns, você encontrou uma Letra", 32)
        verificaAcerto = 0

    print('\n' * 10)
    if ''.join(escolhida) == selecionada:
        caixaTexto(f'Você venceu acertou a palavra -> {selecionada}', 33)
        break
if paraWhile == 6:
    caixaTexto(f'Você Perdeu, a palavra era {selecionada}', 37)
