import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://127.0.0.1:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("World")