# Quiz sobre Tecnologia

## Indice

+ [🎯 Objetivo](#🎯-objetivo)
+ [⚙️ Como rodar](#⚙️-como-rodar)

---

## 🎯 Objetivo

Este projeto tem como objetivo implementar uma aplicação cliente-servidor utilizando sockets TCP em Python. O projeto foi desenvolvido para a disciplina de Redes de Computadores. A proposta de criar um quiz serve para aplicar os conceitos de cliente-servidor, onde o servidor envia as perguntas e o cliente responde, mantendo a conexão ativa até que o cliente deseje encerrá-la.

---

## ⚙️ Como rodar

### Pré-requisitos

- Python 3 instalado na máquina
- Dois terminais abertos simultaneamente

### 🚀 Passo a passo

1. **Clone o repositório**

```bash
git clone https://github.com/viviancalheiros/aplicacao-tcp.git
cd aplicacao-tcp
```

2. **Abra dois terminais**

    + No primeiro terminal, execute o servidor:

    ```bash
    python server.py
    ```

    + No segundo terminal, execute o cliente:

    ```bash
    python client.py
    ```