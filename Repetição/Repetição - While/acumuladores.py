total = 0
contador = 0
valor = 1 
# Lê valores e imprime: soma, quantidade e média
# TODO Esse código tem um erro, qual???
while valor != 0:
    valor = float(input("Qual o valor?"))
    total = total + valor
    contador += 1

print(total,contador,total/contador)