import os
import uuid
import pywhatkit as kt
from tkinter import filedialog
from time import sleep

print('-' * 35)
print('Transformar imagem em ASCII Art!'.center(35))
print('-' * 35)
sleep(1)


def abrirArquivo():
    caminho_arquivo = filedialog.askopenfilename()
    caminho_formatado = caminho_arquivo.replace('/', r'\\')
    return caminho_formatado


def selecionarLocal():
    local = filedialog.askdirectory()
    local_formatado = local.replace('/', r'\\')
    return local_formatado


os.system('cls')
print('Selecione o arquivo')
arquivo = abrirArquivo()
os.system('cls')
print('Selecione onde irá salvar')
sleep(1)
local_salvamento = selecionarLocal() + f'\\{str(uuid.uuid4())}'

try:
    kt.image_to_ascii_art(arquivo, local_salvamento)
    os.system('cls')
    print('Concluido!')
except:
    os.system('cls')
    print('Arquivo não suportado.')
