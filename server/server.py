import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f"Received: {request.decode()}")
        with open("index.html", "r") as file:
            html_content = file.read()
        
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{html_content}"
        client_socket.sendall(response.encode())

if __name__ == "__main__":
    start_server("localhost", 8085)
