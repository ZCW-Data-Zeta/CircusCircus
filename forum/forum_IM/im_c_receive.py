"""
    Client side module to receive connections.
    listen to ports. send data to c_handler.py
    send trigger to client network handler (^)
"""
from im_client import server, nicknames, clients, HOST, PORT
import im_c_handle

import socket
import threading
import im_c_broadcast


def receive():
    while True:  # can expand this to do signal handling
        client, address = server.accept()
        print(f'connected with {str(address)}')

        client.send("NICK".encode('utf-8'))  # will ask for nickname
        nickname = client.recv(1024)

        # room for improvement here, nickname handling can be built out
        clients.append(client)
        nickname.appent(nickname)

        print(f"Nickname of the client is {nickname}")
        im_c_broadcast(f"{nickname} connected to server \n".encode("utf-8"))
        client.send("Connected to server".encode("utf-8"))

        thread = threading.thread(target=im_c_handle, args=(client,))
        # start threading, passing the comma in args= to make tuple
        thread.start()

