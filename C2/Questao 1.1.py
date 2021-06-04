# Faça um código que pergunte uma nota. 
# O código só pode aceitar notas entre 0 e 10 e deve 
# continuar perguntando caso seja 
# digitado um valor fora desse intervalo.

nota = float(input("Qual a nota?"))

while nota < 0 or nota > 10:
    nota = float(input("Qual a nota? [ deve ser entre 0 e 10] "))