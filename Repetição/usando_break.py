import random
cont = 0
# Imprime número aleatório até encontrar um maior que 90

while True:
    numero = random.randint(1,100)
    print(numero)
    cont += 1
    if numero > 90:
        break
