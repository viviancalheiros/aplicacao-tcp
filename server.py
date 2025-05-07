#servidor

from socket import *
import random

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
    'Quem foi o primeiro programador da História?',
    'Qual foi o primeiro protocolo criado?',
    'Quando surgiu o primeiro smartphone?'
    'Qual a rede social mais utilizada no mundo?'
]
opcoes = [
    ['1 -ENIAC\n2 - Pascaline\n3 - UNIVAC\n4 - IBM PC'],
    ['1 - Alan Turing\n2 - Grace Hopper\n3 - Ada Lovelace\n4 - Charles Babbage'],
    ['1 - ARPANET\n2 - NCP\n3 - TCP/IP\n4 - HTTP'],
    ['1 - 2000\n2 - 2005\n3 - 1992\n4 - 1998'],
    ['1 - Instagram\n2 - Whatsapp\n3 - Youtube\n4 - Facebook'],
]
respostas = ['1', '3', '2', '3', '4']
        
while True:
    conn, addr = server.accept()
    print("Servidor conectado!")
    conn.send('Quiz sobre tecnologia!'.encode())
    while True:
        conn.send('1 - Iniciar quiz\n2 - Exibir histórico\n0 - Sair'.encode())
        escolhido = conn.recv(1024).decode()
        if escolhido == '0':
            break
        elif escolhido == '1':
            print('Iniciando quiz...')
            for i in range(5):
                indice = random.randint(0, 10)
                
                conn.send(perguntas[indice].encode())
                conn.send(opcoes[indice][indice].encode())
                
                resposta = conn.recv(1024).decode()
                print(resposta)
        elif escolhido == '2':
            print('Histórico!')
    break

print('Conexão servidor encerrada')
server.close()