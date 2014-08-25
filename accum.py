from multiprocessing.connection import Listener
import RPi.GPIO as io

io.setmode(io.BCM)
pir_pin = 18
io.setup(pir_pin, io.IN)

address = ('localhost', 6000)
listener = Listener(address, authkey='peeping-pi')

while True:
    conn = listener.accept()
    conn.send(io.input(pir_pin))
    conn.close()
