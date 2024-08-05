import socket

def send_request(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(message.encode())
    response = client_socket.recv(1024)
    print(f"Received: {response.decode()}")
    client_socket.close()

if __name__ == "__main__":
    send_request("localhost", 8085, "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")