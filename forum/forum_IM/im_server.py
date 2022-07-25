"""
    Server side setup for instant messaging
"""
import socket
import threading
import im_s_receive
# import time
# import sys
import os
# Set environment variable
os.environ['TK_SILENCE_DEPRECATION'] = '1'

HOST = '127.0.0.1'  # localhost IP
# must hard-code specific local port for communication
PORT = 9090  # port forward to allow LAN communication

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, TCP socket
server.bind((HOST, PORT))  # setup server on IP address constant above


# opens ports to signals
server.listen()

clients = []  # list of client IPs
nicknames = []  # list of user aliases
"""
below is the beginning of flask implementation
"""
#
# import flask as fl
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def message_home():
#     return fl.render_template('IM_home.html')
#
#
# @app.route('/chat')
# def chat_app():
#     username = fl.request.args.get('username')
#     room = fl.request.args.get('room')
#
#     if username and room:
#         return fl.render_template('chat.html')
#     else:
#         return fl.redirect(fl.url_for('home'))
#
#
# if __name__ == '__main':
#     # @app.run(debug=True)
#     pass


if __name__ == '__main__':
    print('server running... ')
    im_s_receive.receive()
