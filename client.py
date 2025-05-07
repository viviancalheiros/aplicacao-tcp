#cliente

from socket import *

host = gethostbyname(gethostname())
port = 12000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

inicio = client.recv(1024).decode()
print(inicio)

while True:
    opcao = client.recv(1024).decode()
    print(opcao)
    escolhido = input()
    client.send(escolhido.encode())
    if escolhido == '0':
        break
    elif escolhido == '1':
        perguntas = client.recv(1024).decode()
        print(perguntas)
        opcoes = client.recv(1024).decode()
        print(opcoes)
        resp = input()
        client.send(resp.encode())

print('Conexão cliente encerrada')
client.close()