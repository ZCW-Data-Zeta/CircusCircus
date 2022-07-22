"""
    Broadcast handler for sending messages to server
"""
from im_client import clients


def broadcast(message):
    for client in clients:
        client.send(message)

