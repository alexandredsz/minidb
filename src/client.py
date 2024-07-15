import socket

# Define constants
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8000        # The port used by the server

def send_command(c, command):
    r"""
    Send a command to the server and print the response.

    Args:
        c (socket.socket): The client socket.
        command (str): The command to send to the server.
    """
    try:
        c.sendall(command.encode() + b'\n')
        response = c.recv(1024)
        print(response.decode())
    except Exception as e:
        print(f"Error sending command: {e}")
    
        
def run_client():
    r"""
    Run the client to connect to the server, send commands, and receive responses.
    """
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.settimeout(3)
    c.connect((HOST, PORT))
    while True:
        command = input("Enter command: ")
        if command == "exit":
            break

        send_command(c, command)
    
    c.close()

if __name__ == "__main__":
    run_client()
