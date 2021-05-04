import socket
import threading
import pickle

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
        print(f"Connected with {client_address}")
        
        client.send('server 1'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        print(f"Nickname of the Client is {nickname}")
        
        client.send('server 2'.encode('utf-8'))
        public_key = client.recv(1024).decode('utf-8')
        
        client.send('server 3'.encode('utf-8'))
        N = client.recv(1024).decode('utf-8')
        
        client_data[nickname] = [client, int(public_key), int(N)]
        client_data_partial[nickname] = [int(public_key), int(N)]

        with open("data.pickle", "wb") as f:
            pickle.dump(client_data_partial, f)

        
        announcement = f"server {nickname} has joined the chat"
        broadcast(announcement)

        client.send("server Connected To Server".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,) )
        thread.start()



print("Server is Running")
main()
