#jogo de advinhação
import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print(f"Você digitou: {chute_str}")
        
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("Seu chute foi maior que o número secreto.")
            elif menor:
                print("Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do jogo!")
    print(f"O número secreto era {numero_secreto}.")
if __name__ == "__main__":
    jogar()

#jogo de adivinhação
# Este é um jogo simples onde o usuário tenta adivinhar um número secreto entre 1 e 100.