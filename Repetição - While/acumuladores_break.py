total = 0
contador = 0
valor = 1 

# Lê valores e imprime: soma, quantidade e média
while True:
    valor = float(input("Qual o valor?"))
    if valor == 0:
        break
    total = total + valor
    contador += 1
print(total,contador,total/contador)
