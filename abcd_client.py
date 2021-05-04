import socket
import threading
from key_generator import generate_keys
from text_to_cipher import decrypt
from client_data_list import client_data

print("hello")
public_key, private_key, N = generate_keys()
nickname = input("choose a nickname: ")


client = socket.socket()
port = 65432
server = client.connect(('127.0.0.1', port))

def receive():
    while True:

        try:
            print("1")
            received_message = client.recv(1024).decode('utf-8')
            print("2")
            sender_nickname, encrypted_message = received_message.split(' ', 1)
            print("3")
            
            print(f"{encrypted_message}")
            print(f"{sender_nickname}")
            
            
            
         

            if sender_nickname == 'server':
                print(f"Please Enter {encrypted_message}")

                if received_message == 'server NICK':
                    client.send(nickname.encode('utf-8'))
                elif received_message == 'server KEY':
                    client.send(str(public_key).encode('utf-8'))
                elif received_message == 'server N':
                    client.send(str(N).encode('utf-8'))
                else:
                    
                    print(f"server {encrypted_message}")
            else:
                encrypted_message = int(encrypted_message)
                message = decrypt(encrypted_message, private_key, N)
                print(f"{sender_nickname}: {message}")

        except Exception as e:
            print(f"an error occured {e}")
            client.close()
            break

def write():
    while True:

        input_message = f'{input("")}'
        receiver_nickname, text = input_message.split(' ', 1)
        encrypted_message = encrypt(int(text), client[receiver_nickname][1], N)
        message = f"{nickname} {encrypted_message}"

        client.send(message.encode('utf-8'))


write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

