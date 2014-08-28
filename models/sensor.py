import RPi.GPIO as io
from multiprocessing import Queue
import time

def run(eventq):
    io.setmode(io.BCM)
    pir_pin = 18
    io.setup(pir_pin, io.IN)

    while True:
        sensed = io.input(pir_pin)
        eventq.put(sensed)
        time.sleep(1)
