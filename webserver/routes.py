from flask import Flask, render_template, jsonify
from multiprocessing import Value
import webserver
import random

@webserver.app.route("/")
def home():
    return render_template('home.html', occupied=webserver.occstate.value)

@webserver.app.route("/isoccupied")
def is_occupied():
    occupied = webserver.occstate.value
    #occupied = bool(random.getrandbits(1))
    return  jsonify({'occupied': occupied, 'msg': current_message(occupied)})

def current_message(occupied):
    if occupied:
        return "Wait your turn."
    else:
        return "It's calling your name!"
