conta = int(input("Qual a conta?"))
soma = 0

while conta != 0:
    soma += conta % 10
    conta //= 10 # soma += conta % 10

print("Digito verificador:",soma % 10)
