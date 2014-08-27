from flask import Flask, render_template
from multiprocessing.connection import Client
app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    address = ('localhost', 6000)
    conn = Client(address, authkey='peeping-pi')
    occupied = conn.recv()
    conn.close()
    return render_template('home.html', occupied=occupied)

def run(occupied):
    app.run(host='0.0.0.0')

if __name__ == "__main__":
    run(None)
