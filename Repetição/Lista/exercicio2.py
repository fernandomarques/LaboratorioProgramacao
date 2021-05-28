# Faça um programa que leia 5 números e informe a soma e a 
# média dos números.

soma = 0

for n in range(5):
    num = float(input("Digite um numero: > "))
    soma = soma + num

print("Soma = ", soma)
print("Media = ", soma/5)
