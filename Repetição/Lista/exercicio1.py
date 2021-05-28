# Faça um programa que leia 5 números e informe o maior número.
## Ler um número 
## Ler um número 5x
## Lógica para o maior

maior = -999

for n in range(5):
    num = float(input("Digite um numero: > "))
    if num > maior:
        maior = num

print("Maior valor =", maior)