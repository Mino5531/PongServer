from NetworkManager import NetworkManager
from DataHandler import DataHandler
from QueueManager import QueueManager


def main():
    dataHandler = DataHandler()
    netMgr = NetworkManager()
    netMgr.InitNet()
    qMgr = QueueManager()
    while True:
        cmd = raw_input("")
        if(cmd == "list"):
            print(NetworkManager.clients)
        if(cmd == "queue"):
            print(QueueManager.instance.getQueue())
        if(cmd == "stop"):
            print("Shutting down server...")
            netMgr.Shutdown()
            break


if __name__ == "__main__":
    main()
