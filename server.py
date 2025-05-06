#servidor

from socket import *

host = gethostbyname(gethostname())
port = 12000

print(f'HOST: {host}, PORT {port}')

#AF_INET = IPv4
#SOCK_STREAM = TCP
#SOCK_DGRAM = UDP
server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(5)

perguntas = [
    'Qual o nome do primeiro computador desenvolvido?',
    'Quem foi o primeiro programador da História?'
]
opcoes = [
    ['1 -ENIAC\n2 - Pascaline\n3 - UNIVAC\n4 - IBM PC'],
    ['1 - Alan Turing\n2 - Grace Hopper\n3 - Ada Lovelace\n4 - Charles Babbage']
]
respostas = ['1', '3']
        

while True:
    conn, addr = server.accept()
    print("Servidor conectado!")
    conn.send('Quiz sobre tecnologia!'.encode())
    while True:
        conn.send('1 - Iniciar quiz\n2 - Exibir histórico\n0 - Sair'.encode())
        msg = conn.recv(1024).decode()
        if msg == '0':
            break
        elif msg == '1':
            print('Iniciando quiz...')
        elif msg == '2':
            print('Histórico!')
    break
print('Conexão servidor encerrada')
server.close()