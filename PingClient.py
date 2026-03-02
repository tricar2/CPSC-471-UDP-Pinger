from socket import* 
import time

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
#setting timeout to 1 second
clientSocket.settimeout(1)

sequenceNumber = 1

while sequenceNumber <= 10:
    roundTrip = time.time()
    message = f"Ping {sequenceNumber} {roundTrip}"

    try:
        clientSocket.send(message.encode(), (serverName, serverPort))
        serverMsg = clientSocket.recv(1024)
        
    except clientSocket.timeout:
        print("Request timed out")

    sequenceNumber += 1

clientSocket.close()