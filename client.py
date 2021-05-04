import socket
import threading
from key_generator import generate_keys
from text_to_cipher import encrypt, decrypt, text_to_numeric_cipher,numeric_cipher_to_text
import pickle

nickname = input("Choose a Nickname: ")
public_key, private_key, N = generate_keys()

client = socket.socket()
port = 12342
client.connect(('127.0.0.1', port))

def close_connection(client_data_partial):

    client_data_partial.pop(nickname.lower())
    with open("data.pickle", "wb") as f:
        pickle.dump(client_data_partial, f)

    client.close()

def show_users(client_data_partial):
    for nickname in client_data_partial.keys():
        print(nickname.capitalize())

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
                decrypted_message = decrypt(int(encrypted_message), private_key, N)             
                decrypted_message = numeric_cipher_to_text(str(decrypted_message))
          
            if sender_nickname == 'server':
                if decrypted_message == 1:
                    client.send(nickname.encode('utf-8'))
                elif decrypted_message == 2:
                    client.send(str(public_key).encode('utf-8'))
                elif decrypted_message == 3:
                    client.send(str(N).encode('utf-8'))
                else:
                    print(f"[{decrypted_message}]")

            else:
                print(f"{sender_nickname.capitalize()}: {decrypted_message}")
                
        except Exception as e:
            print(f"An error has Occured: {e}")

            client_data_partial = {}
            with open("data.pickle", "rb") as f:
                client_data_partial = pickle.load(f)

            close_connection(client_data_partial)
            client.close()
            break


def write():
    while True:
        input_message = f'{input("")}'

        client_data_partial = {}
        
        with open("data.pickle", "rb") as f:
            client_data_partial = pickle.load(f)

        if input_message.lower() == 'leave':
            close_connection(client_data_partial)
            break
            
        elif input_message.lower() == 'show':
            show_users(client_data_partial)

        else:
            try:
                receiver_nickname, input_text = input_message.split(' ', 1)
            
                if receiver_nickname.lower() in client_data_partial.keys():
                    text = text_to_numeric_cipher(input_text)
                    encrypted_message = encrypt(int(text), client_data_partial[receiver_nickname.lower()][0], client_data_partial[receiver_nickname.lower()][1])
                    message = f"{receiver_nickname} {encrypted_message}"

                    client.send(message.encode('utf-8'))

                else:
                    print(f"[No user with nickname {receiver_nickname.capitalize()} present]")

            except:
                print("[Incorrect Message Format]")
                print("Follow - UserNickname Message")


write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()