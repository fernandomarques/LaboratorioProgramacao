# 1. Faça um programa que receba dois números inteiros 
# e gere os números inteiros que estão no intervalo 
# compreendido por eles.

lim_inf = int(input("Limite inferior"))
lim_sup = int(input("Limite superior"))

for i in range(lim_inf, lim_sup+1):
    print(i,end=" ")
    