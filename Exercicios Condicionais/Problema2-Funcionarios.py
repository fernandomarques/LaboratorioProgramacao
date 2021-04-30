
horas = float(input("Quantas horas você trabalhou?"))

valor_hora = 19.5
salario = valor_hora * horas

print(salario)

desconto = 0
if salario > 2500:
    desconto = salario * 0.25
    print("Desconto: R$",desconto)
    
print(f"Salario : R$ {salario - desconto}")
