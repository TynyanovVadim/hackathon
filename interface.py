import PySimpleGUI as sg
import json
import asyncio

from post_module import get_adresses
from vk_module import get_by_id
from telegram_module import get_messages, search

def Save(data):
    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

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
            lat = values[0]
            lon = values[1]
            radius = values[2] if values[2] != 0 else 100
            output(get_adresses(lat, lon, radius))

def TG():
    sg.theme('DarkAmber')

    layout_TG = [ [sg.Text('Заполните поля')],
               [sg.Text('Введите ID группы          '), sg.InputText()],
               [sg.Text('Введите ID пользователя    '), sg.InputText()],
               [sg.Text('Введите ключевое слово     '), sg.InputText()],
               [sg.Button('Search'), sg.Button("History"), sg.Button('Exit')] ]

    window = sg.Window('Modul 2', layout_TG)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'History':
            window.close()
            try:
                output(asyncio.run(get_messages(values[0])))
            except:
                output("ID не найден")
        if event == 'Search':
            window.close()
            try:
                output(asyncio.run(search(values[0], values[2], values[1])))
            except:
                output("ID не найден")

def VK():
    sg.theme('DarkAmber')

    layout_TG = [ [sg.Text('Заполните поля')],
               [sg.Text('Введите ID'), sg.InputText()],
               [sg.Button('Ok'), sg.Button('Exit')] ]

    window = sg.Window('Modul 2', layout_TG)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ok':
            window.close()
            output(get_by_id(values[0]))

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
