morango = float(input("Quantos kilos de morango?"))
maca = float(input("Quantos kilos de maçã?"))

if morango > 5:
    preco_morango = morango * 2.2
else:
    preco_morango = morango * 2.5    
if maca > 5:
    preco_maca = maca * 1.5
else:
    preco_maca = maca * 1.8

preco_total = preco_maca + preco_morango

if maca + morango > 8 or preco_total > 25:
    preco_total = preco_total * 0.9 
    print(r"Pelo volume de compras você tem 10% de desconto")

print("-------------   Total   --------------")
print(f"Maça:    {maca:8.2f} kg - Total R${preco_maca:8.2f}")
print(f"Morango: {morango:8.2f} kg - Total R${preco_morango:8.2f}")
print(f"Total   : {maca+morango:8.2f} kg R${preco_total:8.2f}")