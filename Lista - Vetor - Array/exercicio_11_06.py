# Crie um vetor de tamanho 10
# Preencha o vetor com valores aleatórios
# Calcule a média e a soma do vetor (sem usar sum)
# Encontre o maior e menor valor do vetor (sem usar min e max!)
import random

soma = 0
lista = []
TAMANHO = 10
for i in range(TAMANHO):
    val = random.randint(1,20)
    soma += val
    lista.append(val)
    if i == 0:
        maior = val
        menor = val
    elif val > maior:
        maior = val
    elif val < menor:
        menor = val
media = soma / TAMANHO
print(lista)
print(f"Maior: {maior}\nMenor: {menor}\nSoma: {soma}\nMedia: {media}")
