import socket

headersize = 10
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = client.recv(16)
        if new_msg:
            print(f"new message length : {msg[:headersize]}")
            msglen = int(msg[:headersize])
            new_msg = False
        full_msg += msg.decode("utf-8")

        if len(full_msg) - headersize == msglen:
            print("full message recieved")
            print(full_msg[headersize:])
            new_msg = True
            full_msg = ''

print(full_msg)
