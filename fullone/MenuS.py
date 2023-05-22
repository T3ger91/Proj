import PySimpleGUI as sg
from gamesR import gameR
import time
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
#func of startng GUI with 3 buttons 
#can be used as well as start struc for next GUI
#needed import consol to new window 
def Menu():
    #size stile and color layout 
    layout = [
        [sg.Text('Chose:', size=(30, 1), justification='center')],
        [sg.Button('Play', size=(30, 2))],
        [sg.Button('Rules', size=(30, 2))],
        [sg.Button('Exit', size=(30, 2))]
    ]
    #Name of your window  
    window = sg.Window('Menu', layout)
    #Calling func by button pressing
    while True:
        event, _ = window.read()

        #events by press
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
            #main struc launch 
        elif event == 'Play':
            print(' Starting...')
            time.sleep(1)
            window.close()
            gameR()
            #HTML file opening 
        elif event == 'Rules':
                print(' Rules...')

                def open_html_file(file_path):
                    webbrowser.open(file_path)
                html_file_path = 'Rules.html'
                open_html_file(html_file_path)
                #Bye bye game 
        elif event == 'Exit':
                print(" Bye")
                exit()
        window.close()
