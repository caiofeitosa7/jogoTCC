from tkinter import *
import tkinter.font as tkFont

def form_inicio():
    JUSTIFICA_TEXTO = 'center'
    WIDTH_JANELA = 1000
    HEIGHT_JANELA = 600
    WIDTH_TEXT = 950
    HEIGHT_TEXT = 50
    PADDING = 20
    POS_X = 10
    POS_Y = 10    
    
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    app = Tk()
    fontStyle = tkFont.Font(family="Arial", size=15)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
    
#     app.configure(background = '#fff')
    Label(app, text = 'Você tomou alguma bebida com cafeína nas '
            + 'últimas 5 horas (café, chá preto, chá mate, Coca-Cola)?'
            + ' Em caso afirmativo, qual bebida e há quanto tempo (aproximadamente):',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = fontStyle, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    formInicio_1 = Text(app, width=110, height=2)
    formInicio_1.pack()
    
    Label(app, text = 'Quanto tempo faz desde que você comeu algo pela última vez? Você está com fome?',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = fontStyle, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    
    Label(app, text = 'Você tomou alguma bebida com álcool na última hora (cerveja, vinho etc.)?'
              + ' Não é necessário especificar.',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = fontStyle, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    Label(app, text = 'Você faz uso regular de algum remédio? Se não se incomodar, especifique.'
              + ' (todas as informações fornecidas neste questionário são confidenciais, '
              + 'nos termos do Termo de Consentimento)',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = fontStyle, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    Label(app, text = 'Você tomou algum remédio ou fez uso de droga de qualquer tipo na última hora? '
              + 'Se não quiser, não é necessário especificar, e caso não queira responder a esta pergunta, '
              + 'não há qualquer obrigação. (todas as informações fornecidas neste questionário são '
              + 'confidenciais, de acordo com o Termo de Consentimento)',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = fontStyle, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    
    
    app.mainloop()










if __name__ == '__main__':
    form_inicio()