"""
    Client side setup for instant messaging
"""
import socket
import threading

HOST = '0.0.0.0'  # localhost IP
PORT = 9090  # port forward to allow LAN communication

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, TCP socket
server.bind((HOST, PORT))  # setup server on IP address constant above

clients = []  # list of client IPs
nicknames = []  # list of user aliases

