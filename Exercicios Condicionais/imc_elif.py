
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / (altura*altura)

print("Seu imc é",round(imc,2))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc < 25:
    print("Você está com peso normal")
elif imc < 30:
    print("Você está com acima do peso")
else:
    print("Você está obeso")
