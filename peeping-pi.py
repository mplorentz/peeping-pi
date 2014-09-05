from multiprocessing import Process, Queue, Value
from webserver import webserver
import os, ctypes, models

def main():
    is_occupied = Value(ctypes.c_bool, False)
    eventq = Queue()
    port = int(os.getenv('PEEPING_PI_PORT', 80))
    sensor = Process(target=models.sensor.run, args=(eventq,))
    accumulator = Process(target=models.accumulator.run, args=(eventq, is_occupied))
    server = Process(target=webserver.run, args=(is_occupied, port))

    sensor.start()
    accumulator.start()
    server.start()

if __name__ == "__main__":
    main()
