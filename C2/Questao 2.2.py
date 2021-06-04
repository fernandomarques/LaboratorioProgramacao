# Usando laços de repetição faça um programa que leia os
#  valores de idades de 10 pessoas e indique quem é a 
# pessoa mais velha e quantas idades lidas são maiores que 18


mais_velho = 0
contador = 0
maior_18 = 0

for i in range(10):
    idade = int(input("Qual a sua idade? "))
    if idade > mais_velho:
        mais_velho = idade
    if idade > 18:
        maior_18 += 1 # ou maior_18 = maior_18 +1


print("A pessoa mais velha possui",mais_velho,"anos")
# TODO podemos fazer um if para as condicoes especiais 0 e 1. 
print(f"{maior_18} pessoas possuem idade maior que 18")