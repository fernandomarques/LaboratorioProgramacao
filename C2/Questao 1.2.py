#Faça um código que pergunte uma altura. O código só pode aceitar 
# alturas entre 0 e 3 e deve continuar perguntando caso seja
# digitado um valor fora desse intervalo.


altura = float(input("Qual a altura?"))

while altura < 0 or altura > 3:
    altura = float(input("Qual a altura? [ deve ser entre 0 e 3] "))