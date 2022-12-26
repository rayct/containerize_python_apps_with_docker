# Written By: Raymond Turner @rayturner.dev
# Fast API with a Single endpoint using Docker

import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def central_function():
    return{"Ray": "Colin"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
    




































# import time
# import socket
# from sklearn.datasets import load_iris

# data = load_iris()
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("0.0.0.0", 9999))

# server.listen()

# while True:
#     client, addr = server.accept()
#     print("Connection from" , addr)
#     client.send("You are Connected!\n".encode())
#     client.send(f"{data['data'][:, 0]}\n".encode())
#     time.sleep(2)
#     client.send("You are being disconnected!\n".encode())
#     client.close()
