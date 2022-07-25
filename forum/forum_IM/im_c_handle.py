"""
    client side network handler
"""

from im_client import nicknames, clients
import im_c_broadcast


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[client.index(client)]} is saying {message}" ) # logging statement for server
            # need to develop index of nicknames for server side handling
            # this prints on server console log
            im_c_broadcast(message)
        except:
            # below needs to be handled with SQL
            index = clients.index(client)  # looks up current client
            clients.remove(client)  # remove client from chatroom
            client.close()  # close connection
            nickname = nicknames[index]  # loops up current index
            nicknames.remove(nickname)  # could also use .pop() here
            break  # this ends thread since connection is done
