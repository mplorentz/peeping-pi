import RPi.GPIO as io
from multiprocessing import Queue

class Sensor
    def run(eventq):
        io.setmode(io.BCM)
        pir_pin = 18
        io.setup(pir_pin, io.IN)

        while True:
            eventq.put(io.input(pir_pin))
            sleep(1)
