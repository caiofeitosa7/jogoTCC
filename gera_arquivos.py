import pandas as pd
import openpyxl
import os.path
import os

path = r'resultados/'

def limpa_resultados():
    for arquivo in list(os.listdir(path)):
        os.remove(path + arquivo)
    

def arquivo_analise(perguntas: list, respostas: list, tipo_form: str):
    nome_arquivo = f'formulario_{tipo_form}1'
    
    df = pd.DataFrame({
            'PERGUNTAS': perguntas,
            'RESPOSTAS': respostas
        })
    
    arquivos = list(os.listdir(path))
    quant_analises = max([int(arq.replace('.xlsx', '')[-1]) for arq in arquivos])
    
    if not len(arquivos) or not os.path.exists(f'{path}final{quant_arquivos}'):
        df.to_excel(path + nome_arquivo + '.xlsx', index=False)
    else:
        df.to_excel(path + nome_arquivo[:-1] + str(quant_arquivos + 1) + '.xlsx', index=False)
        


        
