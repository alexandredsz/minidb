import socket
import threading
import os
import pickle
from database import MiniDatabase

# Define constants
HOST = '127.0.0.1'  # Localhost
PORT = 8000         # Port to listen on

def handle_client(conn, addr, db):
    r""" 
    Handles the communication with a connected client.

    Args:
        conn (socket.socket): The client socket connection.
        addr (tuple): The client address.
        db (MiniDatabase): The database instance for processing commands.
    """

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = db.process_command(data.decode())
            conn.sendall(response.encode() + b'\n')

    except Exception as e:
        print(f"Error when hanlding client: {e}")

    finally:
        conn.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")

def run_server():
    r"""
    Sets up and runs the server to listen for incoming connections.
    """
    
    try:
        db = MiniDatabase()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Listening on {HOST}:{PORT}")
        while True:
            conn, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            threading.Thread(target=handle_client, args=(conn, addr, db)).start()

    except Exception as e:
        print(f"Error running server: {e}")

    finally:
        server.close()

if __name__ == "__main__":
    run_server()