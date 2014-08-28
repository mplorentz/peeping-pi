from multiprocessing import Queue, Value
from collections import deque


def run(eventq, occstate):
    occstate.value = False
    # event history is a queue of sensor events with the oldest events on the left side. 
    event_history = deque([], 120)
    fp = open('accumulator.log', 'a')

    while True:
        event = eventq.get()
        event_history.append(event)
        count = 0
        with open('accumulator.log', 'a') as fp:
            for e in event_history:
                fp.write("%d" % (1 if e else 0))
                if e:
                    count += 1
            fp.write('\n')
        oldvalue = occstate.value
        occstate.value = count >= 40
        if oldvalue != occstate.value:
            print("Occupied state changed to %s" % occstate.value)
