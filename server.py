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

historico = []
        
while True:
    conn, addr = server.accept()
    print("Servidor conectado!")
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
            for i in indices:
                pergunta = f'{perguntas[i]}\n' + '\n'.join(opcoes[i])
                conn.send(pergunta.encode())
                
                resposta = conn.recv(1024).decode()
                
                if resposta == respostas[i]:
                    pontos += 1 
                
            if len(historico) >= 5:
                del(historico[0])
                
            historico.append(pontos)
            conn.send(str(pontos).encode())
            
        elif escolhido == '2':
            historico_format = ' | '.join(map(str, historico))
            conn.send(historico_format.encode())
    break

print('Conexão servidor encerrada')
conn.close()
server.close()