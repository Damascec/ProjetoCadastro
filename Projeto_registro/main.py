import PySimpleGUI as sg
from random import randint
import back



sg.theme('random')

def front():
    flayout = [
        [sg.Text('Bem Vindo')],                         # ROW 1
        [sg.Button('ENTRAR'), sg.Button('SAIR')]        # ROW 2

    ]

    window = sg.Window('Human Resources APP', flayout, size=(500, 100), element_justification='center') 
    button, values = window.read()

    if button == 'ENTRAR':
        window.close()

    if button == 'SAIR':
        window.exit() # Fecha o app encerrando todo o processo


NAME = back.read_task()

layout = [
    [sg.Text('Digite o nome do funcionário'), sg.InputText('', key='-NAME-')],
    [sg.Button('Adicionar')],
    [sg.Text('')],
    [sg.Text('Funcionários Cadastrados')],
    [sg.Listbox(NAME, size=(50, 10), key='-BOX-')],
    [sg.Button('Deletar'), sg.Button('Sair')]
]

front()      

window = sg.Window('Main Page', layout)

while True:
    button, values = window.read()

    if button == 'Adicionar':
        ID = randint(1,99)
        NAME = values['-NAME-'].capitalize()

        if NAME != '':
            back.write(ID, NAME)

        NAME = back.read_task()

        window.find_element('-NAME-').Update('')
        window.find_element('-BOX-').Update(NAME)

    if button == 'Deletar':
        if NAME:
            x = values['-BOX-'] [0]
            back.deletar(x)
            NAME = back.read_task()
            window.find_element('-BOX-').Update(NAME)

    if button =='Sair':
        window.close()
        break