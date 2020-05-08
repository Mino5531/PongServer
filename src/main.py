from NetworkManager import NetworkManager
from DataHandler import DataHandler


def main():
    DataHandler.InitDataHandler()
    NetworkManager.InitNet()
    while True:
        cmd = raw_input("")
        if(cmd == "list"):
            print(NetworkManager.clients)
        if(cmd == "stop"):
            print("Shutting down server...")
            NetworkManager.Shutdown()
            break


if __name__ == "__main__":
    main()