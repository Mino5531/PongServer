from Client import Client
import socket
import threading


class NetworkManager:
    # NetMgr socket
    sock = socket.socket()
    # NetMgr listen thread
    runningThread = threading.Thread()
    # NetMgr running?
    running = False
    # Clients
    clients = {}
    # instance
    instance = None

    def __init__(self):
        NetworkManager.instance = self

    def Shutdown(self):
        if(NetworkManager.running):
            NetworkManager.running = False
            NetworkManager.runningThread.join(2)
            NetworkManager.sock.close()

    def InitNet(self):
        NetworkManager.running = True
        NetworkManager.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        NetworkManager.sock.bind(('localhost', 3007))
        NetworkManager.sock.listen(5)
        NetworkManager.runningThread = threading.Thread(
            target=NetworkManager.instance.ListenTcp, args=())
        NetworkManager.runningThread.setDaemon(True)
        NetworkManager.runningThread.start()
        print("NetMgr started")

    def ListenTcp(self):
        while(NetworkManager.running):
            (clientsocket, address) = NetworkManager.sock.accept()
            if(not NetworkManager.running):
                break
            print("Incoming connection from: %s:%i" %
                  (address[0], address[1]))
            NetworkManager.clients[address] = Client(clientsocket, address)
