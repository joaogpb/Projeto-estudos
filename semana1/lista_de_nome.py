def ordenar_palavras(lista_palavras):
    # Ordena ignorando maiúsculas/minúsculas
    return sorted(lista_palavras, key=lambda x: x.lower())

def verificar_ordem(lista_palavras):
    # Verificação: Ordem crescente ignorando maiúsculas/minúsculas
    if lista_palavras == sorted(lista_palavras, key=lambda x: x.lower()):
        print("A lista já está em ordem alfabética (ignorando maiúsculas/minúsculas).")
    else:
        print("A lista NÃO está em ordem alfabética (ignorando maiúsculas/minúsculas). Reorganizando:")
        lista_ordenada = sorted(lista_palavras, key=lambda x: x.lower())
        for palavra in lista_ordenada:
            print(f"'{palavra}'")

# Exemplo de uso:
palavras = [
    'Garuda','Revenant','mag','Gyre','hydroid','Baruck','Oberon','Loki','Gauss',
    'Proteia','Titania','Nova','Sevagoth','Citrine','Lavos','Styanax','Nidus',
    'Qorvex','Hildrin','Kullervo','Caliban','Xaku'
]
verificar_ordem(palavras)
palavras_ordenadas = ordenar_palavras(palavras)
for palavra in palavras_ordenadas:
    print(palavra)