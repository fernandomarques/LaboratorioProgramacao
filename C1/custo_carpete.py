# Faça um programa em Python que leia a área e preço por
#  m² do carpete e calcule e imprima quanto será gasto com carpete. 

area = float(input("Qual a área a ser carpetada?"))
preco = float(input("Qual o custo do carpete?"))

custo = area * preco

print("Custo total: R$", round(custo,2))
print(f"Custo total: R$ {custo:.2f}") # outra forma de fazer

