import qrcode
import PySimpleGUI as sg
import time
from PIL import Image

#entrada de dados
#1- o link que deseja adicionar ao qr CODE
#2- o nome que deseja dar ao arquivo
#por enquanto é isso

janela = [
    [sg.Text('URL')],
    [sg.Input('',key='url_input')],
    [sg.Text('Nome (arquivo.png)')],
    [sg.Input('',key='nome_input')],
    [sg.Button('Gerar QR CODE',key='gerar_bt')],
    [sg.Image('',key='img_qrcode')]
]

window = sg.Window('Gerador de QR CODE').Layout(janela)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'gerar_bt':
        qrcode_link = values['url_input']
        qrcode_name = values['nome_input']

        arquivo = qrcode_name + '.png'

        qr_gerado = qrcode.make(qrcode_link)
        qr_gerado.save(arquivo)



        sg.popup(qr_gerado)
