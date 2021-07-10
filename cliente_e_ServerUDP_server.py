import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

meuhost  = 'localhost'
minhaporta = 5432

s.bind((meuhost, minhaporta))
mensagem = '\nServidor: Olá cliente blz?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados :
        print('Servidor enviando... ')
        s.sendto(dados + (mensagem.encode()), end)


