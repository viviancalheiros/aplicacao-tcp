#cliente

from socket import *

host = gethostbyname(gethostname())
port = 12000 #porta do servidor

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
        for i in range(5):
            pergunta = client.recv(1024).decode()
            print(pergunta)
            
            resp = input()
            client.send(resp.encode())
        pontos = int(client.recv(1024).decode())
        print("Fim do quiz...")
        
        if pontos == 5:
            print("Você ganhou!")
        elif pontos == 0:
            print("Você perdeu!")
        print(f"Pontuação total: {pontos} pontos\n")
    elif escolhido == '2':
        historico = client.recv(1024).decode()
        print(historico)
    else:
        print('Opção inválida. Tente novamente:')
        continue

print('Conexão cliente encerrada')
client.close()