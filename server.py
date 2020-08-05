import socket
import time

headersize = 10


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    print(f"Connection from {addr} has been established!")
    msg = 'This is your server speaking'
    msg = f'{len(msg):<{headersize}}' + msg
    conn.send(bytes(msg, "utf-8"))
    while True:
        time.sleep(3)
        msg = f"The time is : {time.time()}"
        msg = f'{len(msg):<{headersize}}' + msg
        conn.send(bytes(msg, "utf-8"))

    print('Client is no more')