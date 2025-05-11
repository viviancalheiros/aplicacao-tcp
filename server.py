#servidor

from socket import *
from threading import Thread
import random

host = gethostbyname(gethostname())
port = 12000

print(f'HOST: {host}, PORT: {port}')

#AF_INET = IPv4
#SOCK_STREAM = TCP
#SOCK_DGRAM = UDP
server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port)) #associa o IP e a porta ao socket
server.listen(5) #fica com até 5 conexões na fila

#server.settimeout(60) #fecha o servidor após 1 min sem conexão

perguntas = [
    'Qual o nome do primeiro computador desenvolvido?',
    'Quem foi o primeiro programador da História?',
    'Qual foi o primeiro protocolo criado?',
    'Quando surgiu o primeiro smartphone?',
    'Qual a rede social mais utilizada no mundo?',
    'Qual foi o primeiro chatbot criado?',
    'Qual foi a primeira grande marca de computadores?',
    'Qual protocolo de redes é utilizado para o envio de e-mails?',
    'Qual foi a primeira linguagem de programação de alto nível?',
]
opcoes = [
    ['1 - ENIAC\n2 - Pascaline\n3 - UNIVAC\n4 - IBM PC'],
    ['1 - Alan Turing\n2 - Grace Hopper\n3 - Ada Lovelace\n4 - Charles Babbage'],
    ['1 - ARPANET\n2 - NCP\n3 - TCP/IP\n4 - HTTP'],
    ['1 - 2000\n2 - 2005\n3 - 1992\n4 - 1998'],
    ['1 - Instagram\n2 - Whatsapp\n3 - Youtube\n4 - Facebook'],
    ['1 - ChatGPT\n2 - Eliza\n3 - Siri\n4 - Watson'],
    ['1 - Apple\n2 - Microsoft\n3 - Xerox\n4 - IBM'],
    ['1 - FTP\n2 - POP3\n3 - IMAP\n4 - SMTP'],
    ['1 - FORTRAN\n2 - COBOL\n3 - C\n4 - BASIC'],
    
]
respostas = ['1', '3', '2', '3', '4', '2', '4', '4', '1']

historico = {}
        
def iniciarJogo (conn, addr):
    client = f'{addr[0]} e porta {addr[1]}'
    historico[client] = []
    print(f"[+] Servidor conectado ao cliente {client}")
    conn.send('Quiz sobre tecnologia!'.encode())
    
    while True:
        pontos = 0
        conn.send('1 - Iniciar quiz\n2 - Exibir histórico\n0 - Sair'.encode())
        escolhido = conn.recv(1024).decode()
        if escolhido == '0':
            break
        elif escolhido == '1':
            print('Iniciando quiz...')
            indices = random.sample(range(len(perguntas)), 5)
            cont = 1
            for i in indices:
                pergunta = f'{cont}) {perguntas[i]}\n' + '\n'.join(opcoes[i])
                conn.send(pergunta.encode())
                
                resposta = conn.recv(1024).decode()
                
                if resposta == respostas[i]:
                    pontos += 1 
                cont += 1
                
            if len(historico[client]) >= 5:
                del(historico[client][0])
                
            historico[client].append(pontos)
            conn.send(str(pontos).encode())
        elif escolhido == '2':
            if (len(historico[client]) == 0): 
                historico_format = 'Não há dados no histórico'
            else: 
                historico_format = ' | '.join(map(str, historico[client]))
            conn.send(historico_format.encode())
        else:
            continue
    conn.close()
    print(f'Conexão servidor com cliente {client} encerrada')
    
while True:
    conn, addr = server.accept()
    thread = Thread(target = iniciarJogo, args = (conn, addr))
    thread.start()