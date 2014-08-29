from flask import Flask, render_template, jsonify
from multiprocessing import Value
import webserver, messages
import random

@webserver.app.route("/")
def home():
    return render_template('home.html', occupied=webserver.occstate.value)

@webserver.app.route("/isoccupied")
def is_occupied():
    occupied = webserver.occstate.value
    #occupied = bool(random.getrandbits(1))
    return  jsonify({'occupied': occupied, 'msg': messages.current_message(occupied)})

