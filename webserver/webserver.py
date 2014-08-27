from flask import Flask
from multiprocessing import Value

occstate = None
app = Flask(__name__)
app.debug=True

def run(shared_occupancy_state):
    import routes
    global occstate
    occstate = shared_occupancy_state
    app.run('0.0.0.0')
