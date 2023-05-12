#main choises menu on the start of the game, ui and other staff plugins must be on place to start it 
def choisemain():
    import webbrowser
    global solution
    solution = ()
    #layout = [
      #  [sg.Text('Choose:', size=(30, 1), justification='center')],
      #  [sg.Button('Play', size=(30, 2))],
      #  [sg.Button('Rules', size=(30, 2))],
      #  [sg.Button('Exit', size=(30, 2))]
   # ]
    #main logic and inic of window to chose what u whant to do normaly play, rules, exit
    def startmain():

        window = sg.Window('Menu', layout)
        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 'Exit'):
                solution = 0
                break
            elif event == 'Play':
                solution = 1
                print('Starting...')
            elif event == 'Rules':
                solution = 2
                print('Loading...')

        window.close()
