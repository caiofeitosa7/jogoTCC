import pandas as pd
import openpyxl
import os

path = r'resultados/'

def limpa_resultados():
    for arquivo in list(os.listdir(path)):
        os.remove(arquivo)
    

def arq_form_inicio(perguntas: list, respostas: list):
    nome_arquivo = 'formulario_inicio1'
    
    df = pd.DataFrame({
            'PERGUNTAS': perguntas,
            'RESPOSTAS': respostas
        })
    
    arquivos = list(os.listdir(path))
    
    if not len(arquivos):
        df.to_excel(path + nome_arquivo + '.xlsx', index=False)
    else:
        quant_arquivos = [int(arq.replace('.xlsx', '')[-1]) for arq in arquivos].max()
        df.to_excel(nome_arquivo + str(quant_arquivos + 1) + '.xlsx')
        
