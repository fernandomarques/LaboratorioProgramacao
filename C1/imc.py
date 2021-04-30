# Faça um programa em Python  que leia o peso e a altura de uma pessoa e calcule 
# o IMC do usuário. Lembrando que o IMC é o peso dividido pela altura ao quadrado.

peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / (altura*altura)

print("Seu imc é",round(imc,2))