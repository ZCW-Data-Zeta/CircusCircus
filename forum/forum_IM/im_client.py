"""
    Client side setup for instant messaging
"""
import socket
import threading

import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import os
# Set environment variable
os.environ['TK_SILENCE_DEPRECATION'] = '1'

HOST = '0.0.0.0'  # localhost IP
PORT = 9090  # port forward to allow LAN communication

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, TCP socket
server.bind((HOST, PORT))  # setup server on IP address constant above

clients = []  # list of client IPs
nicknames = []  # list of user aliases

class Client:

    def __init__(self, host, port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        # opens pop-up.
        msg = tkinter.Tk()
        msg.withdraw()  # not best practices

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)

        # flag to allow GUI open
        self.gui_done = False
        # flag to end GUI
        self.running = True

        # gui interactive thread
        gui_thread = threading.Thread(target=self.gui_loop)
        # deals with server connection
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    # front end for chat interface
    # must be built out, then built into web forum
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")  # to configure window

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText()
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')  # bad implementation
        # when state = disabled, cannot change content
        # needs to be state= default, then make the change, then enabled

        self.text_area = tkinter.Label(self.win, text="Message: ", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=5)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.input_area.pack(padx=20, pady=5)

        self.gui_done = True
        # try to pull gui configuration from templates
        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

        # pass

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}" # weird syntax, be sure to read up
        # can change message function to be server side
        # better implementation to get message and then assign nick via DB
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')
        # pass

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)
        # pass


# starts client connection
client = Client(HOST, PORT)
