import sys
import gera_arquivos
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

respostas = []
respostasFormFinal = []

perguntas = (
        '  1 – Quanto tempo, em minutos e segundos, você acha que jogou,'
            + ' desde a mensagem de início do jogo?       \n  Formato = 00:00',
        '2 - Em uma escala de 1 a 5 onde 1 representa nenhuma diversão e 5 representa muita'
                + ' diversão, qual nota você atribuiria a este jogo?'
                + '                              ',
        '  3 - O que poderia ser feito para torná-lo mais divertido?'
                + '                                            '
                + '                                            ',
    )


def salva_respostas():    
    for resposta in respostas:
        respostasFormFinal.append(resposta.get('1.0', 'end'))
    
    gera_arquivos.excel_formulario(perguntas, respostasFormFinal, 'final')
    gera_arquivos.compacta_arquivos()
    sys.exit()

    
def form_final():
    app = Tk()
    app.attributes('-fullscreen', True)
    
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    FONT_STYLE = tkFont.Font(family="Helvetica", size=17)
    FONT_STYLE_INPUT = tkFont.Font(family="Helvetica", size=12)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
#     app.configure(background = '#fff')

    Label(app, text=" ").pack()
    
    Label(app, text = '          RESPONDA O QUESTIONÁRIO ABAIXO PARA CONCLUIR',
                justify=JUSTIFICA_TEXTO, anchor='w', font=FONT_STYLE, pady=10,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    Label(app, text=" ").pack()
    
    Label(app, text = perguntas[0],
                justify=JUSTIFICA_TEXTO, anchor='w', font=FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    respostas.append(Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT))
    respostas[0].pack()
    
    Label(app, text = perguntas[1],
                justify=JUSTIFICA_TEXTO, anchor='w', font=FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    respostas.append(Text(app, width=WIDTH_INPUT, height=2, font=FONT_STYLE_INPUT))
    respostas[1].pack()
    
    Label(app, text = perguntas[2],
                justify=JUSTIFICA_TEXTO, anchor='w', font=FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    respostas.append(Text(app, width=WIDTH_INPUT, height=2, font=FONT_STYLE_INPUT))
    respostas[2].pack()
    
    for i in range(7):
        Label(app, text=" ").pack()
    
    button_border = Frame(app, highlightbackground="black", highlightthickness=2, bd=0)
    Button(button_border, text='Finalizar', command=salva_respostas, font=FONT_STYLE, padx=30).pack()
    button_border.pack()
        
    app.mainloop()
    
if __name__ == '__main__':
    form_final()
