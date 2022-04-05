import PySimpleGUI as sg

questao1 = 'Você tomou alguma bebida com cafeína nas ' \
            + 'últimas 5 horas (café, chá preto, chá mate, Coca-Cola)?' \
            + ' Em caso afirmativo, qual bebida e há quanto tempo (aproximadamente):'
            
layout = [  [sg.Text(questao1)],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('    Ok    ')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()  
