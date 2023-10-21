
import os
import shutil

DIRETORIO_ORIGEM = 'Caminho_para_seu_diretorio'
EXTENSOES_MAPEADAS = {
    'Imagens': ['.jpg', '.jpeg', '.png'],
    'Músicas': ['.mp3', '.wav'],
    'Vídeos': ['.mp4', '.mkv'],
}

for diretorio in EXTENSOES_MAPEADAS.keys():
    if not os.path.exists(os.path.join(DIRETORIO_ORIGEM, diretorio)):
        os.makedirs(os.path.join(DIRETORIO_ORIGEM, diretorio))

relatorio = {diretorio: 0 for diretorio in EXTENSOES_MAPEADAS.keys()}
relatorio['Outros'] = 0

for arquivo in os.listdir(DIRETORIO_ORIGEM):
    if os.path.isfile(os.path.join(DIRETORIO_ORIGEM, arquivo)):
        extensao = os.path.splitext(arquivo)[1]
        diretorio_destino = None
        
        for diretorio, extensoes in EXTENSOES_MAPEADAS.items():
            if extensao in extensoes:
                diretorio_destino = diretorio
                break
        
        if diretorio_destino:
            shutil.move(os.path.join(DIRETORIO_ORIGEM, arquivo), os.path.join(DIRETORIO_ORIGEM, diretorio_destino))
            relatorio[diretorio_destino] += 1
        else:
            if not os.path.exists(os.path.join(DIRETORIO_ORIGEM, 'Outros')):
                os.makedirs(os.path.join(DIRETORIO_ORIGEM, 'Outros'))
            shutil.move(os.path.join(DIRETORIO_ORIGEM, arquivo), os.path.join(DIRETORIO_ORIGEM, 'Outros'))
            relatorio['Outros'] += 1

for diretorio, quantidade in relatorio.items():
    print(f"{diretorio}: {quantidade} arquivos movidos.")
