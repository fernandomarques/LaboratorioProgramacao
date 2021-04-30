media_aluno = float(input("Qual a média do aluno?"))

aulas = int(input("Quantas aulas tiveram?"))
faltas = int(input("Quantas faltas o aluno teve?"))

presenca = (aulas - faltas) / aulas

if presenca < 0.75:
    print("Reprovado por falta")
elif media_aluno >= 6:
    print("Aprovado")
else:
    print("Reprovado por nota")


if presenca >= 0.75 and media_aluno >= 6:
    print("Aprovado")
elif media_aluno < 6:
    print("Reprovado por nota")
else:
    print("Reprovado por falta")
