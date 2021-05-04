import socket
import threading
from client_data_list import client_data

server = socket.socket()
port = 65432
host = '127.0.0.1'
server.bind(('', port))
server.listen(5)

def communicate(message, client):
    client.send(message.encode('utf-8'))

def broadcast(message):
    for client_nickname, client_info in client_data.items():
        message = f"server {message}"
        print(type(client_nickname))
        print(type(client_info))
        print(type(client_info[0]))
        client_info[0].send(message.encode('utf-8'))

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            receiver_nickname, client_message = message.split(' ', 1)
            client_message = int(client_message)

            sender_nickname =""
            for client_nickname in client_data.keys():
                if client_data[client_nickname][0] == client:
                    sender_nickname = client_nickname

            
            client_message = f'{sender_nickname} {client_message}'
            communicate(str(client_message), client_data[receiver_nickname][0])

        except Exception as e:
            print(f"{e}")
            # index = clients.index(client)
            # clients.remove(client)
            # client.close()

            for client_nickname in client_data.keys():
                if client_data[client_nickname][0] == client:
                    sender_nickname = client_nickname

            announcement = f"{sender_nickname} has left the chat"
            broadcast(announcement)

            client_data.pop(sender_nickname)
            break

def main():
    while True:
        client, address = server.accept()
        print(f"connected with{str(address)}")
        print(f"the type of client is {client}")

        client.send('server NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        client.send('server KEY'.encode('utf-8'))
        public_key = client.recv(1024).decode('utf-8')

        client.send('server N'.encode('utf-8'))
        N = client.recv(1024).decode('utf-8')

        client_data[nickname] = [client , public_key, N]

        print(f"nickname of the client is {nickname}")
        message = f"{nickname} has joined the chat"

        broadcast(message)
        client.send("connected to server".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,) )
        thread.start()


print("Server is running")
main()