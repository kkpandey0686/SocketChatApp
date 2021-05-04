import socket
import threading
from key_generator import generate_keys
from text_to_cipher import encrypt, decrypt, text_to_numeric_cipher,numeric_cipher_to_text
import pickle


public_key, private_key, N = generate_keys()
nickname = input("Choose a Nickname: ")

client = socket.socket()
port = 13234
client.connect(('127.0.0.1', port))


def receive():
    while True:
        try:
            received_message = client.recv(1024).decode('utf-8') 
            sender_nickname, encrypted_message = received_message.split(' ', 1)

            if sender_nickname == 'server':
                if encrypted_message.isdigit():
                    decrypted_message = int(encrypted_message)
                else:
                    decrypted_message = encrypted_message 
            else:
                print("hello1")
                decrypted_message = decrypt(int(encrypted_message), private_key, N)
                print("hello2")
                decrypted_message = numeric_cipher_to_text(str(decrypted_message))
 
            print("hello")
            if sender_nickname == 'server':
                if decrypted_message == 1:
                    client.send(nickname.encode('utf-8'))
                elif decrypted_message == 2:
                    client.send(str(public_key).encode('utf-8'))
                elif decrypted_message == 3:
                    client.send(str(N).encode('utf-8'))
                else:
                    print(received_message)

            else:
                print("yes")
                
                print(f"{sender_nickname.capitalize()}: {decrypted_message}")
                
        except Exception as e:
            print(f"An error has Occured: {e}")
            client.close()
            break


def write():
    while True:
        input_message = f'{input("")}'
        receiver_nickname, input_text = input_message.split(' ', 1)
        
        text = text_to_numeric_cipher(input_text)
        
        client_data_partial = {}
        

        with open("data.pickle", "rb") as f:
            client_data_partial = pickle.load(f)

        encrypted_message = encrypt(int(text), client_data_partial[receiver_nickname][0], client_data_partial[receiver_nickname][1])
        message = f"{receiver_nickname} {encrypted_message}"

        client.send(message.encode('utf-8'))


write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()