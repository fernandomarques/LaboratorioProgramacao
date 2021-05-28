# Lê uma nota, se ela não estiver entre 0 e 10, pede 
# para o usuário digitar outra nota

nota1 = float(input("Qual a nota 1?"))

while nota1 > 10 or nota1 < 0:
    print("A nota deve ser entre 0 e 10")
    nota1 = float(input("Qual a nota 1?"))

print("Nota",nota1)