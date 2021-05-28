# 1. Altere o programa anterior para mostrar no final a soma dos números.

lim_inf = int(input("Limite inferior"))
lim_sup = int(input("Limite superior"))

soma = 0
for i in range(lim_inf, lim_sup+1):
    print(i,end=" ")
    soma += i

print("Soma ", soma)
    