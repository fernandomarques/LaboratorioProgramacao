# Usando laços de repetição faça um programa que leia os preços de itens de um 
# carrinho de compra (pode ler só 10)  e indique o total da compra e
#  qual foi o item mais barato. 


mais_barato = 0
contador = 0
soma = 0

for i in range(3):
    preco = float(input("Qual o preco? "))
    soma = soma + preco # ou soma += preco
    if preco < mais_barato or i == 0:
        mais_barato = preco

print(f"O total da compra é R${soma}")
# TODO podemos fazer um if para as condicoes especiais 0 e 1. 
print(f"O item mais barato custa R${mais_barato}")