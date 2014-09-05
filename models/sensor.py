import RPi.GPIO as io
from multiprocessing import Queue
import time, os

# Number of seconds between reading the sensor
sensor_interval = 1 

# GPIO pin the IR sensor is on (using the Broadcom numbering system).
pir_pin = int(os.getenv('PEEPING_PI_PIN', 18))

def run(eventq):
    """ Sensor.py reads the IR sensor at the specified interval and adds an event to
    the eventq for the accumulator to interpret. Currently, the events are simply a 
    boolean indicating whether movement was sensed during the last sampling. """
    io.setmode(io.BCM)
    io.setup(pir_pin, io.IN)

    while True:
        eventq.put(io.input(pir_pin))
        time.sleep(sensor_interval)
