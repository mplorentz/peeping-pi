from multiprocessing.connection import Listener
from multiprocessing import Queue

class Accumulator
    def run(eventq, port, randomword):
        address = ('localhost', port)
        listener = Listener(address, authkey='peeping-pi')

        while True:
            conn = listener.accept()
            conn.send(q.get)
            conn.close()
