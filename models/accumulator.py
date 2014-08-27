from multiprocessing.connection import Listener
from multiprocessing import Queue, Value

def run(eventq, occstate):
    occstate.value = True
