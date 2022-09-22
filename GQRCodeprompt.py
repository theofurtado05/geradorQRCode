import qrcode
import time

print('-==GERADOR DE QR CODE==-')
print('1º Passo - Digitar o link que deseja (https://seusite.com)')
print('2º Passo - Digitar o nome que deseja salvar o arquivo (arquivo.png)')
time.sleep(1)

link = input('Digite o link: ')
id = input('Digite o nome do arquivo: ')

qr = qrcode.make(link)

qr.save(id)
