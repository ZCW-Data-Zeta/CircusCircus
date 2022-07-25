import threading
from im_server import clients, nicknames, server
import im_s_handle as sh
import im_s_broadcast as bd


def receive():
    while True:  # can expand this to do signal handling
        client, address = server.accept()
        print(f'connected with {str(address)}') # server logging of message

        client.send("NICK".encode('utf-8'))  # will ask for nickname
        nickname = client.recv(1024)

        # room for improvement here, nickname handling can be built out
        clients.append(client)
        nicknames.append(nickname)

        print(f"Nickname of the client is {nickname}")
        bd.broadcast(f"{nickname} connected to server \n".encode("utf-8"))
        client.send("Connected to server".encode("utf-8"))

        thread = threading.Thread(target=sh.handle, args=(client,))
        # start threading, passing the comma in args= to make tuple
        thread.start()
