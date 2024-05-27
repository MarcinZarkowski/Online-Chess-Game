import socket
import pickle

class Network:
    def __init__(self):
        self.client =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server =socket.gethostbyname(socket.gethostname())#if running server and clients on the same network this should be fine.(replace with server IP adress if otherwise)
        self.port = 5050
        self.addr = (self.server, self.port)
        self.whoWon=None
        self.HowWon=None
        self.piece = None
        self.ID=self.piece
        
        self.NumberofPlayers=0

    def getPiece(self):
        return self.piece

    def connect(self):
     
        try:
            self.client.connect(self.addr)
            message=self.client.recv(2048).decode('utf-8')
            
            myId=message[0]

            
            
            HowManyPlayers=int(message[2])
            self.NumberofPlayers=HowManyPlayers
            
            
            self.piece=myId
        except Exception as e:
            print("Couldn't connect:", e)
            self.piece= None

    def getNumOfPlayer(self):
        try:
            self.client.send("getNumofPlayers".encode('utf-8'))
            message=self.client.recv(2048).decode('utf-8')
            
            self.NumberofPlayers=int(message)
            
        except socket.error as e:
            message="error"
            return message
    
    def getCurrentTurn(self):
        try:
            self.client.send("getCurrentTurn".encode('utf-8'))
            
            message=self.client.recv(2048).decode('utf-8')
            
            return message
            
           

        except socket.error as e:
        
            print(e)
            
    def getBoard(self):
        try:
            self.client.send("getCurrentBoard".encode('utf-8'))  
            message=pickle.loads(self.client.recv(2048*9))
            return message
            
            
        except socket.error as e:
            print(e)

    def send(self, data):
       
        try:
            self.client.send("sendBoard".encode('utf-8'))
            self.client.sendall(pickle.dumps(data))
           
            board=pickle.loads(self.client.recv(2048*20))
            return board
        except socket.error as e:
            print(e)
            return None
    def oponentWins(self, ID, LostHow):
        try:
            sendthis=ID+LostHow
            self.client.send("Ilost".encode('utf-8'))
            self.client.send(sendthis.encode('utf-8'))
            
        except socket.error as e:
            print(e)

    def getGameState(self):
        try:
            self.client.send("WhoWon".encode('utf-8'))
            Winner=self.client.recv(2048).decode('utf-8')
            print("Winner is ", Winner)
            if Winner=='w' or Winner=='b':
                WonHow=self.client.recv(2048).decode('utf-8')
                self.whoWon=Winner
                self.HowWon=WonHow
                print (self.whoWon, self.HowWon)
                
            
        except socket.error as e:
            print(e)
    def disconnect(self):
        self.client.close()
