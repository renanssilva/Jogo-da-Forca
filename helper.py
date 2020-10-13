from random import choice


def carregaPalavras():
    palavras = []
    with open('palavras.txt', 'r') as file:
        leia = file.read()
        for i in leia.split('\n'):
            palavras.append(i)
    return palavras


def selecionaPalavra(palavras):
    return choice(palavras)


def caixaTexto(palavras, cor=30):
    tamanho = (len(palavras) + 13)
    print(f'\33[{cor}m{tamanho * "-"}\n|     {palavras}      |\n{tamanho * "-"}\33[m')


def chances(n):
    print("""
    -----
        |""")
    print("""        O
       /I\\
       / \\
    """[0:n * 6])
