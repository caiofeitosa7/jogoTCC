import pandas as pd
import openpyxl
import os.path
import zipfile
import os

path = r'resultados/'


def limpa_resultados():
    for arquivo in list(os.listdir(path)):
        os.remove(path + arquivo)
    

def arquivo_analise(direcoes_corretas: list, direcoes_personagem: list, tempo_gasto):
    dir_corretas = pd.DataFrame({'DIRECOES_CORRETAS': direcoes_corretas})
    dir_personagem = pd.DataFrame({'DIRECOES_ESCOLHIDAS': direcoes_personagem})
    tempo_jogo = pd.DataFrame({'TEMPO_DE_JOGO': [tempo_gasto]})
    
    writer = pd.ExcelWriter(f'{path}analise_jogo.xlsx', engine='openpyxl')
    
    dir_corretas.to_excel(writer, sheet_name='Análise do Jogador', index=False)
    
    dir_personagem.to_excel(
        writer,
        index=False,
        sheet_name='Análise do Jogador',
        startcol = dir_corretas.shape[1] + 1
    )
    
    tempo_jogo.to_excel(
        writer,
        index=False,
        sheet_name='Análise do Jogador',
        startcol = dir_corretas.shape[1] + dir_personagem.shape[1] + 2
    )

    writer.close()


def excel_formulario(perguntas: list, respostas: list, tipo_form: str):    
    nome_arquivo = f'formulario_{tipo_form}'
    
    df = pd.DataFrame({
            'PERGUNTAS': perguntas,
            'RESPOSTAS': respostas
        })

    df.to_excel(path + nome_arquivo + '.xlsx', index=False, sheet_name=f'Formulario {tipo_form}')


def compacta_arquivos():
    proxima_analise = len([arq for arq in os.listdir(path) if arq.endswith('.zip')]) + 1
    arquivos_excel = [arq for arq in os.listdir(path) if arq.endswith('.xlsx')]
    
    arquivo_zip = zipfile.ZipFile(f'{path}Analise{proxima_analise}.zip', 'w', zipfile.ZIP_DEFLATED)
    
    for arquivo in arquivos_excel:
        arquivo_zip.write(path + arquivo)
        os.remove(path + arquivo)
    
    arquivo_zip.close()
