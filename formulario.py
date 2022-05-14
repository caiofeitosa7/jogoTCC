from tkinter import *
import tkinter.font as tkFont

JUSTIFICA_TEXTO = 'left'
WIDTH_JANELA = 1000
HEIGHT_JANELA = 600
WIDTH_TEXT = 950
HEIGHT_TEXT = 50
WIDTH_INPUT = 120
PADDING = 20
POS_X = 10
POS_Y = 10

form = ''
sairFormulario = False
arrayInputs = [i for i in range(5)]
respostasFormInicio = []

app = Tk()

def fecha_janela():
    global sairFormulario
    
    if sairFormulario:
        print('entrou')
        sys.exit()


def salvar(lista):
    for resposta in arrayInputs:
        lista.append(resposta.get('1.0', 'end'))
        print(resposta.get('1.0', 'end'))
    
    
def salvaRespostas():
    global form, sairFormulario, app
    
    sairFormulario = True
    
    if form == 'inicio':
        salvar(respostasFormInicio)
    elif form == '':
        pass
    
    fecha_janela()
    

def form_inicio():
    global form, sairFormulario, app
    
    form = 'inicio'
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    FONT_STYLE = tkFont.Font(family="Arial", size=13)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
    
#     app.configure(background = '#fff')
    Label(app, text = '1 - Você tomou alguma bebida com cafeína nas '
            + 'últimas 5 horas (café, chá preto, chá mate, Coca-Cola)?'
            + ' Em caso afirmativo, qual\nbebida e há quanto tempo (aproximadamente):',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[0] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[0].pack()
    
    Label(app, text = '2 - Quanto tempo faz desde que você comeu algo pela última vez? Você está com fome?'
                + '                                                                 ',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[1] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[1].pack()
    
    Label(app, text = '3 - Você tomou alguma bebida com álcool na última hora (cerveja, vinho etc.)?'
              + ' Não é necessário especificar.                                       ',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[2] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[2].pack()
    
    Label(app, text = ' 4 - Você faz uso regular de algum remédio? Se não se incomodar, especifique.'
              + ' (todas as informações fornecidas neste questionário são confidenciais, '
              + 'nos termos do Termo de Consentimento)',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[3] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[3].pack()
    
    Label(app, text = '5 - Você tomou algum remédio ou fez uso de droga de qualquer tipo na última hora? '
              + 'Se não quiser, não é necessário especificar,\ne caso não queira responder a esta pergunta, '
              + 'não há qualquer obrigação. (todas as informações fornecidas neste questionário são '
              + 'confidenciais, de acordo com o Termo de Consentimento)',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[4] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[4].pack()
    
#     tkinter.Button(app, text = "Print", command = salvaRespostas)
    Button(app, text='Pronto', command=salvaRespostas, font=FONT_STYLE, padx=30).pack()
    
    app.mainloop()


arrayInputs = [i for i in range(5)]

def form_final():
    global form, sairFormulario
    
    form = 'inicio'
    posix = WIDTH_JANELA // 6
    posiy = HEIGHT_JANELA // 14
    
    FONT_STYLE = tkFont.Font(family="Arial", size=15)
    
    app.title('Lost Kingdom')
    app.geometry(f'{WIDTH_JANELA}x{HEIGHT_JANELA}+{posix}+{posiy}')
    
    Label(app, text = '1 – Quanto tempo, em minutos e segundos, você acha que jogou,'
                + ' desde a mensagem de início do jogo?       \nExemplo = 00:00',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[0] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[0].pack()
    
    Label(app, text = '1 – Quanto tempo, em minutos e segundos, você acha que jogou,'
                + ' desde a mensagem de início do jogo?       \nExemplo = 00:00',
                justify = JUSTIFICA_TEXTO, anchor = 'w', font = FONT_STYLE, pady=15,\
                padx=PADDING-10, wraplength=WIDTH_JANELA).pack()
    
    arrayInputs[0] = Text(app, width=WIDTH_INPUT, height=2)
    arrayInputs[0].pack()
    
    app.mainloop()
    
    



if __name__ == '__main__':
    form_inicio()
#     app = Tk()
#     form_final()