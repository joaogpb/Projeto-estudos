#calculo do IMC (Índice de Massa Corporal)

peso = int(input("Ingrese seu peso em kg: "))
altura = float(input("Ingrese sua altura em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print(f"Seu IMC é {imc:.2f}, você está com o peso normal.")
elif 25 <= imc < 29.9:
    print(f"Seu IMC é {imc:.2f}, você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade grau 2.")
else:
    print(f"Seu IMC é {imc:.2f}, você está com obesidade grau 3.")