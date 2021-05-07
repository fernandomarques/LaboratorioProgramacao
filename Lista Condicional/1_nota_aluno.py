nota1 = float(input("Qual a primeira nota?"))
nota2 = float(input("Qual a segunda nota?"))

media = (nota1 + nota2)/2

print("Média = ",media)
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")