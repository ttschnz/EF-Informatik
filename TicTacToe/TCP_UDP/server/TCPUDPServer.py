import socket as sk

class Server:
    def __init__(self, protocol, port):
        if protocol.upper() not in ["TCP", "UDP"]: # fuck all other protocols
            raise ValueError('Unknown prococol')
        
        self.PROTOCOL = protocol.upper() 
        # SOCK_STREAM means that it is a TCP socket
        # SOCK_DGRAM means that it is a UDP socket
        self.socketServer =  sk.socket(sk.AF_INET, sk.SOCK_DGRAM if protocol == "UDP" else sk.SOCK_STREAM)
        self.port = port

    def listen(self, callback):
        self.socketServer.bind(("", self.port))

        if self.PROTOCOL == "UDP":
            while True:
                message, clientAddress = self.socketServer.recvfrom(2048) # wait for messages
                print("message from {0}: '{1}'".format(clientAddress, message))
                response = callback(message, clientAddress)
                sk.socket.sendto(response.encode(), clientAddress) # respond
        else:
            self.socketServer.listen(1)
            while True:
                connectionSocket, clientAddress = self.socketServer.accept()
                message = connectionSocket.recv(2048).decode()
                print("message from {0}: '{1}'".format(clientAddress, message))

                response = callback(message, clientAddress)
                connectionSocket.send(response.encode())

                connectionSocket.close()