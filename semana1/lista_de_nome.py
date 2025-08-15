def ordenar_palavras(lista_palavras):
    return sorted(lista_palavras)

def verificar_ordem(lista_palavras):
    # Verificação 1: Ordem crescente padrão
    if lista_palavras == sorted(lista_palavras):
        print("A lista já está em ordem alfabética (case-sensitive).")
    else:
        print("A lista NÃO está em ordem alfabética (case-sensitive). Reorganizando:")
        lista_ordenada = sorted(lista_palavras)
        for palavra in lista_ordenada:
            print(f"'{palavra}'")

    # Verificação 2: Ordem crescente ignorando maiúsculas/minúsculas
    if lista_palavras == sorted(lista_palavras, key=lambda x: x.lower()):
        print("A lista já está em ordem alfabética (ignorando maiúsculas/minúsculas).")
    else:
        print("A lista NÃO está em ordem alfabética (ignorando maiúsculas/minúsculas). Reorganizando:")
        lista_ordenada = sorted(lista_palavras, key=lambda x: x.lower())
        for palavra in lista_ordenada:
            print(f"'{palavra}'")

    # Verificação 3: Ordem decrescente ignorando maiúsculas/minúsculas
    if lista_palavras == sorted(lista_palavras, key=lambda x: x.lower(), reverse=True):
        print("A lista está em ordem alfabética reversa (ignorando maiúsculas/minúsculas).")
    else:
        print("A lista NÃO está em ordem alfabética reversa (ignorando maiúsculas/minúsculas). Reorganizando:")
        lista_ordenada = sorted(lista_palavras, key=lambda x: x.lower(), reverse=True)
        for palavra in lista_ordenada:
            print(f"'{palavra}'")

# Exemplo de uso:
palavras = ['Garuda','Revenant','mag','Gyre','hydroid','Baruck','Oberon','Loki','Gauss','Proteia','Titania','Nova','Sevagoth','Citrine','Lavos','Styanax','Nidus','Qorvex','Hildrin','Kullervo','Caliban','Xaku'
]
verificar_ordem(palavras)
palavras_ordenadas = ordenar_palavras(palavras)
for palavra in palavras_ordenadas:
    print(palavra)