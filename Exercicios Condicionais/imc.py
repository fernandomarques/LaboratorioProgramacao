
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / (altura*altura)

print("Seu imc é",round(imc,2))

if imc < 18.5:
    print("Você está abaixo do peso")

if (18.5 <= imc) and (imc < 25):
    print("Você está com peso normal")

if (25 <= imc) and (imc < 30):
    print("Você está com acima do peso")

if imc >= 30:
    print("Você está obeso")

