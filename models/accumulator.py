from multiprocessing import Queue, Value
from collections import deque


def run(eventq, is_occupied):
    """ The accumulator is a logic element that collects data from sensor.py and 
    decides from the aggregated data whether or not the room is occupied. It makes 
    its findings available to the webserver via the shared variable 'is_occupied'."""

    # event_history is a queue of sensor events with the oldest events on the left side. 
    # Currently, sensor events are just booleans that indicate whether movement was sensed.
    event_history = deque([], 120)
    is_occupied.value = False
    fp = open('accumulator.log', 'a')

    while True:
        total_movement = 0
        consec_stillness = 0

        event = eventq.get()
        event_history.append(event)
        fp.write("%d" % (1 if event else 0))

        for e in event_history:
            if e is True:
                total_movement += 1
                consec_stillness = 0
            else:
                consec_stillness += 1

        oldvalue = is_occupied.value
        if total_movement >= 40 and not is_occupied.value:
            is_occupied.value = True
        if consec_stillness > 60 and is_occupied.value:
            is_occupied.value = False

        if oldvalue != is_occupied.value:
            fp.write("\nState changed to %s\n" % is_occupied.value)
        fp.flush()
