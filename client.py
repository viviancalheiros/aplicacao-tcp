#cliente

from socket import *

host = gethostbyname(gethostname())
port = 12000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

msg = client.recv(1024).decode()
print(msg)

while True:
    msg = client.recv(1024).decode()
    print(msg)
    op = input()
    client.send(op.encode())
    if op == '0':
        break
    elif op == '1':
        resp = input()

print('Conexão cliente encerrada')
client.close()