# Faça um código que pergunte uma idade. O código só pode
#  aceitar idades entre 0 e 200 e deve continuar perguntando
#  caso seja digitado um valor fora desse intervalo.

idade = float(input("Qual a idade?"))

while idade < 0 or idade > 200:
    idade = float(input("Qual a idade? [ deve ser entre 0 e 200] "))