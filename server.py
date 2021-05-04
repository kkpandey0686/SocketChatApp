import socket
import threading
import pickle
# from client_data_list import client_data

server = socket.socket()
port = 13234
server.bind(('',port))
server.listen(5)

client_data = {}
client_data_partial = {}


def find_client_nickname(client):
    for nickname in client_data.keys():
        if client_data[nickname][0] == client:
            return nickname


def print_database():
    print("in print database")
    for nickname in client_data.keys():
        print(f"{nickname}")
        print(f"{type(nickname)}")
        print(f"{client_data[nickname][0]}")
        print(f"{client_data[nickname][1]}")
        print(f"{client_data[nickname][2]}")
        
    print("out of print database")

def communicate(sender_client, message):

    receiver_nickname, encrypted_message = message.split(' ', 1)
    receiver_client = client_data[receiver_nickname][0]
    sender_client_nickname = find_client_nickname(sender_client)
    updated_message = f"{sender_client_nickname} {encrypted_message}"

    receiver_client.send(updated_message.encode('utf-8'))

def broadcast(message):

    for nickname in client_data.keys():
        receiver_client = client_data[nickname][0]
        receiver_client.send(message.encode('utf-8'))

def handle_client(client):
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            communicate(client, message)

        except Exception as e:
            client_nickname = find_client_nickname(client)
            print(e)

            announcement = f"server {client_nickname} has left the chat"
            broadcast(announcement)
            client_data.pop(client_nickname)
            client_data[client_nickname].close()


def main():
    while True:
        client, client_address = server.accept()
        print(f"connected with {client_address}")
        print("in server 1")
        
        client.send('server 1'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        print(f"nickname of the client is {nickname}")
        print("in server 2")
        
        client.send('server 2'.encode('utf-8'))
        public_key = client.recv(1024).decode('utf-8')
        print("in server 3")
        
        client.send('server 3'.encode('utf-8'))
        N = client.recv(1024).decode('utf-8')
        print("in server 4")
        
        client_data[nickname] = [client, int(public_key), int(N)]
        client_data_partial[nickname] = [int(public_key), int(N)]

        print(f"{type(client_data[nickname])} {type(client_data)}, {type(nickname)}, {type(client)}, {type(int(public_key))}, {type(int(N))}")
        print_database()

        with open("data.pickle", "wb") as f:
            pickle.dump(client_data_partial, f)

        
        print("in server 5")

        
        announcement = f"server {nickname} has joined the chat"
        broadcast(announcement)
        print("in server 6")

        client.send("connected to server".encode('utf-8'))
        print("in server 7")
        thread = threading.Thread(target=handle_client, args=(client,) )
        print("in server 8")
        thread.start()



print("Server is running")
main()
