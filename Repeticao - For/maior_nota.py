maior = -1
for i in range(5):
    nota = float(input("Digite uma nota "))
    if nota > maior:
        maior = nota

print(f"Maior nota foi {maior}")