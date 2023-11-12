import PySimpleGUI as sg
import json
def Save(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

def Mail():
    sg.theme('DarkAmber')

    layout_Mail = [ [sg.Text('Заполните поля')],
                    [sg.Text('Введите широту '), sg.InputText()],
                    [sg.Text('Введите долготу'), sg.InputText()],
                    [sg.Text('Введите радиус '), sg.InputText()],
                    [sg.Button('Ok'), sg.Button('Exit')] ]

    window = sg.Window('Modul 1', layout_Mail)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ok':
            window.close()
            output(values) # #коммент ниже

def TG():
    sg.theme('DarkAmber')

    layout_TG = [ [sg.Text('Заполните поля')],
               [sg.Text('Введите IP-адрес группы          '), sg.InputText()],
               [sg.Text('Введите IP-адрес пользователя'), sg.InputText()],
               [sg.Button('Ok'), sg.Button('Exit')] ]

    window = sg.Window('Modul 2', layout_TG)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ok':
            window.close()
            output(values) # В значении должн быть указан конечный итог. Output только печатает исходник

def VK():
    sg.theme('DarkAmber')

    layout_TG = [ [sg.Text('Заполните поля')],
               [sg.Text('Введите IP-адрес'), sg.InputText()],
               [sg.Button('Ok'), sg.Button('Exit')] ]

    window = sg.Window('Modul 2', layout_TG)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ok':
            window.close()
            output(values) #коммент выше

def output(text):
    sg.theme('DarkAmber')

    layout = [ [sg.Text('Вывод')],
            [sg.Text(text)],
            [sg.Button('Save'), sg.Button('Exit')] ]

    window = sg.Window('Кейс 5', layout, size=(700, 500))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
        if event == 'Save':
            Save(text)
            print("Save")
            window.close()

#main
sg.theme('DarkAmber')

layout = [ [sg.Text('Выберите нужный вариант')],
           [sg.Button('Mail'), sg.Button('Telegram'), sg.Button('VK')] ]

window = sg.Window('Кейс 5', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Mail':
        window.close()
        Mail()
    if event == 'Telegram':
        window.close()
        TG()
    if event == 'VK':
        window.close()
        VK()
