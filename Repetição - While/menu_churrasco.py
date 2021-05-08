'''
1 - Quantidade Homens
2 - Quantidade Mulheres
3 - Quantidade crianças
4 - Há bebida alcoolica?
5 - Carne
'''
homens, mulheres, criancas = 4,4,3
bebida = "não"
carne = ""

boi = ' '
frango = ' '
linguica = ' '
porco = ' '
opcoes_carne = 0

while True:
    print(f'''------------- CHURRASCOMETRO ------------------------------------
|    1 - Quantidade Homens:   {homens}
|    2 - Quantidade Mulheres: {mulheres}
|    3 - Quantidade crianças: {criancas}
|    4 - Há bebida alcoolica? {bebida}
|    5 - Carne: [{carne}]
|    6 - Calcular
|    0 - Sair
-----------------------------------------------------------------
    ''')
    escolha = int(input("Digite uma opção\n>"))
    if escolha == 0:
        break
    elif escolha == 1:
        homens = int(input("Quantos homens?\n>"))
    elif escolha == 2:
        mulheres = int(input("Quantas mulheres?\n>"))
    elif escolha == 3:
        criancas = int(input("Quantas crianças?\n>"))
    elif escolha == 4:
        bebida = input("Tem bebida alcoolica? sim / não: ")
        while bebida != "sim" and bebida != "não":
            bebida = input("Escreva 'sim' ou 'não \n>")
    elif escolha == 5:
        while True:
            print(f'''1 - Carne de Boi [{boi}]
2 - Carne de Frango [{frango}]
3 - Carne de Porco [{porco}]
4 - Linguiça [{linguica}]
5 - Sair
''')
            opcao = int(input("> "))
            # TODO se a opção já estiver marcada, desmarcar
            if opcao == 1:
                boi = "X"
                carne += "Boi "
                opcoes_carne += 1
            elif opcao == 2:
                frango = "X"
                carne += "Frango "
                opcoes_carne += 1
            elif opcao == 3:
                porco = "X"
                carne += "Porco "
                opcoes_carne += 1
            elif opcao == 4:
                linguica = "X"
                carne += "Linguiça "
                opcoes_carne += 1
            elif opcao == 5:
                break
    elif escolha == 6:
        break

'''
    Carnes ->  Homens 350, Mulheres 250, Criancas 150
    Bebibidas -> Se alcool 5 Latas Mulher/Homem, 350 ml por criança
            -> Se não 350 ml todo mundo
'''

if escolha == 6:
    if bebida == "sim":
        latas = 3 * (homens + mulheres)
        refri = 250 * criancas
        print(f"Comprar {latas} latas e {refri}ml de refrigerante")
    else:
        refri = 350 * (homens+mulheres+criancas)
        print(f"Comprar {refri}ml de refrigerante")

    carnes = homens * 350 + mulheres * 250 + criancas * 150
    carnes_por_opcao = carnes / opcoes_carne
    if "Boi" in carne:
        print(f"\t{carnes_por_opcao}g de boi")
    if "Frango" in carne:
        print(f"\t{carnes_por_opcao}g de frango")
    if "Porco" in carne:
        print(f"\t{carnes_por_opcao}g de porco")
    if "Linguiça" in carne:
        print(f"\t{carnes_por_opcao}g de linguiça")


