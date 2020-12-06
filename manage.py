from PersonalBase import create_server
from os.path import exists
from os.path import isdir
from os import mkdir

socketIOServer, app = create_server()

if __name__ == '__main__':
    if not (exists("data") and isdir("data")):
        print("data folder not exists, creating...")
        mkdir("data")

    socketIOServer.run(app, debug=True, host="0.0.0.0", port=5000)
