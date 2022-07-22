from im_server import clients


# manage message signal
def broadcast(message):
    for client in clients:
        client.send(message)

# this needs to be expanded to allow for images, reactions, etc
