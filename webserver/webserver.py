from flask import Flask
from multiprocessing import Value

is_occupied = None
app = Flask(__name__)
app.debug=False

def run(shared_is_occupied, port=80):
    """ The webserver serves pages indicating the occupancy state of the room, and
    communicates with the accumulator via the shared variable 'shared_is_occupied'."""
    import routes
    global is_occupied
    is_occupied = shared_is_occupied
    app.run('0.0.0.0', port=port, use_reloader=False)
