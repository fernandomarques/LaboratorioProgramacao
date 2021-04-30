# Faça um programa que leia peso, altura e nome e imprima
#  o nome e o imc da pessoa

nome = input("Qual o seu nome?")
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura?"))
imc = peso / (altura ** 2)
print(f"Olá {nome}, seu imc é: {imc:.2f}") #f-string para facilitar
