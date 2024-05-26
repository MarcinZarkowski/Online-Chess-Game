import socket
from _thread import *
import pickle
from board import Board
import threading

# Get the server IP address
server = socket.gethostbyname(socket.gethostname())
port = 5050

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket options to reuse the address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sock.bind((server, port))
    print(f"Socket bound to {server}:{port}")
except socket.error as e:
    print(f"Socket binding error: {str(e)}")
    exit()

try:
    sock.listen(2)
    print("Socket is now listening for connections")
except socket.error as e:
    print(f"Socket listening error: {str(e)}")
    exit()

print("Waiting for players, Server activated and searching")

WhiteTurn = True
BlackTurn = False

currentBoard = Board(8, 8)

NumofPlayer = 0

ConnectedClients = []

# Initialize a lock for thread safety
#lock = threading.Lock()

def threaded_client(conn, player):
    global WhiteTurn
    global BlackTurn
    global NumofPlayer
    global currentBoard
    global WhiteWon
    WhiteWon = False
    global BlackWon
    BlackWon = False

    if player == 1:
        color = 'w'
    elif player == 2:
        color = 'b'
    SendThis = color + " " + str(NumofPlayer)
    conn.send(SendThis.encode('utf-8'))

    ConnectedClients.append(conn)

    while True:
        data=None
        try:
            data = conn.recv(2048 * 1000)

            if not data:
                break  # Client has disconnected

            decoded_data = data.decode('utf-8')

            if decoded_data == "getNumofPlayers":
                conn.send(str(NumofPlayer).encode('utf-8'))

            elif decoded_data =="getCurrentTurn":
               
                if WhiteTurn:
                    conn.send("w".encode('utf-8'))
                elif BlackTurn:
                    conn.send("b".encode('utf-8'))

            elif decoded_data =="getCurrentBoard":
                conn.sendall(pickle.dumps(currentBoard))

            elif decoded_data=="Ilost":
                ID_data = conn.recv(2048)
                if ID_data.decode('utf-8') == 'w':
                    BlackWon= True
                elif ID_data.decode('utf-8') == 'b':
                    WhiteWon =True

            elif decoded_data == "WhoWon":
                if WhiteWon:
                    conn.send('w'.encode('utf-8'))
                elif BlackWon:
                    conn.send('b'.encode('utf-8'))
                else:
                    conn.send('none'.encode('utf-8'))

            elif decoded_data== "sendBoard":
                # Receive the pickled board object
                board_data =conn.recv(2048 * 10)
                currentBoard =pickle.loads(board_data)

                if WhiteTurn:
                    WhiteTurn =False
                    BlackTurn =True
                elif BlackTurn:
                    BlackTurn=False
                    WhiteTurn =True

                
                conn.sendall(pickle.dumps(currentBoard))

        except Exception as e:
            print(f"Error: {str(e)}")
            break

    print("Lost connection")
    #with lock:
    NumofPlayer-=1
    ConnectedClients.remove(conn)
    currentBoard =Board(8, 8)
    WhiteTurn = True
    BlackTurn = False   
    
    conn.close()

while True:
    try:
        conn, addr = sock.accept()
        print("Connected to this address: ", addr)
        
        if NumofPlayer > 1:
            print("Max players reached")
            conn.close()
        else:
            #with lock:
            NumofPlayer += 1
            start_new_thread(threaded_client, (conn, NumofPlayer))
            print(NumofPlayer)
    except Exception as e:
        print(f"Error accepting connections: {str(e)}")
        break

sock.close()