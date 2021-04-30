# Faça um programa que leia um número inteiro e mostre o seu triplo,
#  sua metade, a sua raiz cúbica e, por fim, o número elevado a potência 2/3

numero = int(input("Digite um numero"))

print(f"O triplo é {numero * 3}")
print(f"A metade é {numero / 2}")
print(f"A raiz cúbica é {numero ** (1/3)}")
print(f"Elevado a 2/3 {numero ** (2/3)}")