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
        movement_count = 0
        nothing_sensed = 0
        with open('accumulator.log', 'a') as fp:
            for e in event_history:
                fp.write("%d" % (1 if e else 0))
                if e:
                    movement_count += 1
                    nothing_sensed = 0
                else:
                    nothing_sensed += 1
            fp.write('\n')
            oldvalue = occstate.value
            if movement_count >= 40 and not occstate.value:
                occstate.value = True
            elif nothing_sensed > 60 and occstate.value:
                occstate.value = False

            if oldvalue != occstate.value:
                fp.write("Occupied state changed to %s" % occstate.value)
