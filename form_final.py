from tkinter import *
import tkinter.font as tkFont

JUSTIFICA_TEXTO = 'left'
WIDTH_JANELA = 1100
HEIGHT_JANELA = 600
WIDTH_TEXT = 980
HEIGHT_TEXT = 50
WIDTH_INPUT = 120
PADDING = 20
POS_X = 10
POS_Y = 10

arrayInputs = []
respostasFormFinal = []

app = Tk()
app.attributes('-fullscreen', True)


def salvaRespostas():
    for resposta in arrayInputs:
        respostasFormFinal.append(resposta.get('1.0', 'end'))
    
    app.destroy()
    

def form_final():
    global app, arrayInputs
    
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    FONT_STYLE = tkFont.Font(family="Helvetica", size=17)
    FONT_STYLE_INPUT = tkFont.Font(family="Helvetica", size=12)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
#     app.configure(background = '#fff')


    Label(app, text = '          RESPONDA O QUESTIONÁRIO ABAIXO PARA CONCLUIR',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=10,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()

    Label(app, text = '1 – Quanto tempo, em minutos e segundos, você acha que jogou,'
                + ' desde a mensagem de início do jogo?       \nFormato = 00:00',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs.append(Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT))
    arrayInputs[0].pack()
    
    Label(app, text=" ").pack()
    
    button_border = Frame(app, highlightbackground = "black", highlightthickness = 2, bd=0)
    Button(button_border, text='Pronto', command=salvaRespostas, font=FONT_STYLE, padx=30).pack()
    button_border.pack()
    
    app.mainloop()


if __name__ == '__main__':
    form_final()
