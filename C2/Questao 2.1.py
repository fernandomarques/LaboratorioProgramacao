# Usando laços de repetição faça um programa que leia as
#  notas C1 e C2 de 10 alunos e imprima as médias para cada aluno
#  lido e conte quantos possuem média acima de 7.

soma = 0
contador = 0
maior_7 = 0

for i in range(10):
    c1 = float(input("Qual a sua nota em C1? "))
    c2 = float(input("Qual a sua nota em C2? "))
    media = (c1+c2)/2
    soma = soma + media
    contador +=1
    if media > 7:
        maior_7 += 1 # ou maior_7 = maior_7 +1


media = soma / contador
print(media)
# TODO podemos fazer um if para as condicoes especiais 0 e 1. 
print(f"{maior_7} alunos tiveram nota maior que 7")