from multiprocessing import Process, Queue
from models import Sensor, Accumulator
from webserver import webserver
import os

port = 6000

def main():
    eventq = Queue()
    randomword = os.urandom(80)
    occupied = False
    sensor = Process(target=Sensor.run, args=(eventq,))
    accum  = Process(target=Accumulator.run, args=(eventq, occupied))
    server = Process(target=webserver.run, args=(occpied,))
    sensor.start()
    accum.start()
    server.start()

if __name__ == '__main__':
    main()
