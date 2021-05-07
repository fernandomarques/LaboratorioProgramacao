# Código criado pelo aluno
#  Wellington Da Silva Barbosa Junior
#

import PySimpleGUI as sg

layout = [[sg.Text("Quantos Kg de morango você quer?"), sg.Text("Quantos Kg de maçã você quer?")],
          [sg.Input(size=(30,1), key='Strawberries'), sg.Input(size=(30,1), key='Apples')],
          [sg.Text("Valor a pagar: R$0.00", size=(40,1), key='Output')],
          [sg.Button('Ok'), sg.Button('Quit')]]

window = sg.Window("Calculadora de Preço", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    strawberries, apples = float(values['Strawberries']), float(values['Apples'])
    frutas = strawberries + apples

    if strawberries <= 5:
        strawb_val = 2.5 * strawberries
    else:
        strawb_val = 2.2 * strawberries
    
    if apples <= 5:
        apple_val = 1.8 * apples
    else:
        apple_val = 1.5 * apples

    pagar = strawb_val + apple_val

    if frutas > 8 or pagar > 25:
        pagar *= 0.9

    window['Output'].update(f"Valor a pagar: R${pagar:.2f}")

window.close()