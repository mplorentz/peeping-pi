from multiprocessing import Process, Queue, Value
import models
from webserver import webserver
import os, ctypes

def main():
    shared_occupancy_state = Value(ctypes.c_bool, False)
    eventq = Queue()
    port = int(os.getenv('PEEPING_PI_PORT', 80))
    sensor = Process(target=models.sensor.run, args=(eventq,))
    accumulator = Process(target=models.accumulator.run, args=(eventq, shared_occupancy_state))
    server = Process(target=webserver.run, args=(shared_occupancy_state, port))

    sensor.start()
    accumulator.start()
    server.start()

if __name__ == "__main__":
    main()
