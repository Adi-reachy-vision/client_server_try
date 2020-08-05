import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data_encode = conn.recv(4096)
        data = data_encode.decode()
        if not data: break
        from_client += data
        print(from_client)
        stringss = "This is your server speaking"
        sen = stringss.encode()
        conn.send(sen)
    conn.close()
    print('Client is no more')