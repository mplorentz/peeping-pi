import RPi.GPIO as io
from multiprocessing import Queue
import time

def run(eventq):
    io.setmode(io.BCM)
    pir_pin = 18
    io.setup(pir_pin, io.IN)

    while True:
        eventq.put(io.input(pir_pin))
        time.sleep(1)
