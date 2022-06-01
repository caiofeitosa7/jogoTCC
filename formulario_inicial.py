from tkinter import *
import tkinter.font as tkFont
import gera_arquivos

JUSTIFICA_TEXTO = 'left'
WIDTH_JANELA = 1100
HEIGHT_JANELA = 600
WIDTH_TEXT = 980
HEIGHT_TEXT = 50
WIDTH_INPUT = 120
PADDING = 20
POS_X = 10
POS_Y = 10

arrayInputs = [i for i in range(5)]
respostasFormInicio = []

perguntas = (
        '1 - Você tomou alguma bebida com cafeína nas '
            + 'últimas 5 horas (café, chá preto, chá mate, Coca-Cola)?'
            + ' Em caso afirmativo, qual bebida e há quanto tempo (aproximadamente):',
        '2 - Quanto   tempo   faz   desde   que   você   comeu   algo   pela   última   vez?      Você   está   com   fome?'
            + '                                                           ',
        '3 - Você tomou alguma bebida com álcool na última hora (cerveja, vinho etc.)?'
            + ' Não é necessário especificar.',
        '4 - Você faz uso regular de algum  remédio?  Se  não  se  incomodar,  especifique.'
            + '  (todas  as  informações fornecidas neste questionário são confidenciais, '
            + 'nos termos do Termo de Consentimento)                             ',
        '5 - Você tomou algum remédio ou fez uso de droga de qualquer tipo na última hora? '
            + 'Se  não  quiser,  não  é necessário especificar, e caso não queira responder a esta pergunta, '
            + 'não há qualquer obrigação. (todas as informações fornecidas neste questionário são '
            + 'confidenciais, de acordo com o Termo de Consentimento)'        
    )

app = Tk()
app.attributes('-fullscreen', True)


def salvaRespostas():
    for resposta in arrayInputs:
        respostasFormInicio.append(resposta.get('1.0', 'end').strip())

    gera_arquivos.arquivo_analise(perguntas, respostasFormInicio, 'inicio')
    app.destroy()
    

def form_inicio():
    global app
    
    form = 'inicio'
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    FONT_STYLE = tkFont.Font(family="Helvetica", size=17)
    FONT_STYLE_INPUT = tkFont.Font(family="Helvetica", size=12)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
#     app.configure(background = '#fff')


    Label(app, text = '         RESPONDA O QUESTIONÁRIO ABAIXO PARA PROSSEGUIR',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=10,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()

    Label(app, text = perguntas[0],
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[0] = Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT)
    arrayInputs[0].pack()
    
    Label(app, text = perguntas[1],
                justify = JUSTIFICA_TEXTO, font = FONT_STYLE, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[1] = Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT)
    arrayInputs[1].pack()
    
    Label(app, text = perguntas[2],
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[2] = Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT)
    arrayInputs[2].pack()
    
    Label(app, text = perguntas[3],
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[3] = Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT)
    arrayInputs[3].pack()
    
    Label(app, text = perguntas[4],
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[4] = Text(app, width=WIDTH_INPUT, height=2, font = FONT_STYLE_INPUT)
    arrayInputs[4].pack()
    
    Label(app, text=" ").pack()
    
    button_border = Frame(app, highlightbackground = "black", highlightthickness = 2, bd=0)
    Button(button_border, text='Pronto', command=salvaRespostas, font=FONT_STYLE, padx=30).pack()
    button_border.pack()
    
    app.mainloop()


if __name__ == '__main__':
    form_inicio()