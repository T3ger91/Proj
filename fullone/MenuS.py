import PySimpleGUI as sg
from gamesR import gameR
import time
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def Menu():
    layout = [
        [sg.Text('Chose:', size=(30, 1), justification='center')],
        [sg.Button('Play', size=(30, 2))],
        [sg.Button('Rules', size=(30, 2))],
        [sg.Button('Exit', size=(30, 2))]
    ]

    window = sg.Window('Menu', layout)

    while True:
        event, _ = window.read()


        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Play':
            print(' Starting...')
            time.sleep(1)
            window.close()
            gameR()
        elif event == 'Rules':
                print(' Rules...')

                def open_html_file(file_path):
                    webbrowser.open(file_path)
                html_file_path = 'Rules.html'
                open_html_file(html_file_path)
        elif event == 'Exit':
                print(" Bye")
                exit()
        window.close()
