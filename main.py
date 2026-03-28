import qrcode
import time
import os
import sys

while True:
    print("== GERADOR DE QR CODE == v0.1")
    time.sleep(1)
    print("Este script permite criar QRCodes apenas inserindo o link desejado para que ele se torne um QRCode")
    time.sleep(2)

    linkCriar = input("Insira seu link: ")
    time.sleep(1)
    nomeLink = input("Crie um nome para o arquivo: ")
    time.sleep(1)
    print("Aguarde...")
    time.sleep(2)
    print("Gerando QRCode...")

    qrPronto = qrcode.make(linkCriar)

    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    qr_folder = os.path.join(base_path, "QRImage")

    os.makedirs(qr_folder, exist_ok=True)

    qrPronto.save(os.path.join(qr_folder, f"{nomeLink}.png"))

    print(f"QRCode criado com sucesso! (Enviado para a pasta: {qr_folder})")
    print("\n" + "="*40 + "\n")