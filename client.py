import socket
import threading
from key_generator import generate_keys
from text_to_cipher import encrypt, decrypt
import pickle
# from server import client_data


public_key, private_key, N = generate_keys()
nickname = input("choose a nickname: ")


client = socket.socket()
port = 13234
client.connect(('127.0.0.1', port))


# def print_database():
#     print("in print database")
#     for nickname in client_data_partial.keys():
#         print(f"{nickname}")
#         print(f"{type(nickname)}")
#         print(f"{client_data_partial[nickname][0]}")
#         print(f"{client_data_partial[nickname][1]}")
        
        
#     print("out of print database")


def receive():
    while True:
        try:
            received_message = client.recv(1024).decode('utf-8') 
            sender_nickname, encrypted_message = received_message.split(' ', 1)
            print(f"received_message is {received_message}")
            print(f"sender_nickname is {sender_nickname}")
            print(f"encrypted_message is {encrypted_message}")

            if sender_nickname == 'server':
                print("is server")
                if encrypted_message.isdigit():
                    print("is digit")
                    decrypted_message = int(encrypted_message)
                else:
                    print("is not a digit")
                    decrypted_message = encrypted_message 
            else:
                print("is not server")
                if encrypted_message.isdigit():
                    print("is digit")
                    decrypted_message = decrypt(int(encrypted_message), private_key, N)
                else:
                    print("is not a digit")
                    decrypted_message = encrypted_message 

            if sender_nickname == 'server':
                print("it is a sender message")
                if decrypted_message == 1:
                    print("message is 1")
                    client.send(nickname.encode('utf-8'))
                elif decrypted_message == 2:
                    print("message is 2")
                    client.send(str(public_key).encode('utf-8'))
                elif decrypted_message == 3:
                    print("message is 3")
                    client.send(str(N).encode('utf-8'))
                else:
                    print("message is 4")
                    print(received_message)

            else:
                print("is not a server message")
                print(f"{sender_nickname} {decrypted_message}")
                
        except Exception as e:
            print(f"an error occured {e}")
            client.close()
            break


def write():
    while True:
                                                # client_data[nickname][0]
        input_message = f'{input("")}'
        receiver_nickname, text = input_message.split(' ', 1)
        

        client_data_partial ={}

        with open("data.pickle", "rb") as f:
            client_data_partial = pickle.load(f)

        # print_database()

        encrypted_message = encrypt(int(text), client_data_partial[receiver_nickname][0], client_data_partial[receiver_nickname][1])
        message = f"{receiver_nickname} {encrypted_message}"

        client.send(message.encode('utf-8'))


write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread = threading.Thread(target=receive)
receive_thread.start()