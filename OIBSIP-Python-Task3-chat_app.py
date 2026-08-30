import socket, threading, time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 55555

# Server code jo background mein chalega
def run_server():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(2)
    clients = []
    while True:
        c, _ = s.accept()
        clients.append(c)
        def handle(client):
            while True:
                try:
                    msg = client.recv(1024)
                    if not msg: break
                    for other in clients:
                        if other != client: other.send(msg)
                except: break
            if client in clients: clients.remove(client)
        threading.Thread(target=handle, args=(c,), daemon=True).start()

threading.Thread(target=run_server, daemon=True).start()
time.sleep(0.5) # Server start hone ka wait

# Client code jisse tum chat karoge
name = input("Naam dalo: ")
client = socket.socket()
client.connect((HOST, PORT))
print("Chat shuru! Message likho aur Enter dabao (Jane ke liye 'quit' likho):")

def listen():
    while True:
        try:
            m = client.recv(1024).decode()
            if not m: break
            print(m)
        except: break

threading.Thread(target=listen, daemon=True).start()

while True:
    text = input()
    if text.lower() == 'quit': 
        client.close()
        break
    time_now = datetime.now().strftime("%H:%M")
    client.send(f"[{time_now}] {name}: {text}".encode())