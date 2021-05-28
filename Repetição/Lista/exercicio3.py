# 1. Faça um programa que imprima na tela apenas os números ímpares
#  entre 1 e 50.

# Forma um: configurando o range
for i in range(1,50,2):
    print(i)

# Forma dois: usando um if e o %
for i in range(1,51):
    if i % 2 != 0: # não é divisível por 2
        print(i)
