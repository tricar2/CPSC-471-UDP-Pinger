from socket import* 
import time

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
#setting timeout to 1 second
clientSocket.settimeout(1)

sequenceNumber = 1
roundTrip = 0

while sequenceNumber <= 10:
    sendTime = time.time()
    message = f"Ping {sequenceNumber} {sendTime}"

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
      
        serverMsg, address = clientSocket.recvfrom(1024)  
        # When msg was received 
        receiveTime = time.time()
        print(f"{serverMsg.decode()}, round trip: {receiveTime - sendTime}")

    except clientSocket.timeout:
        print("Request timed out")

    sequenceNumber += 1

clientSocket.close()