valores = []
for i in range(5):
    valor = int(input("Digite um valor"))
    valores.append(valor)

print(valores)
print("máximo",max(valores))
print("min",min(valores))
print("soma",sum(valores))
print("quantidade",len(valores))
print("media",sum(valores) / len(valores))