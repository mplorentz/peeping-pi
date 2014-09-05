from flask import Flask, render_template, jsonify
from multiprocessing import Value
import webserver, messages, random

@webserver.app.route("/")
def home():
    return render_template('home.html')

@webserver.app.route("/isoccupied")
def is_occupied():
    safe_is_occupied = is_occupied.value
    #safe_is_occupied = bool(random.getrandbits(1)) # used for development
    return  jsonify({
        'occupied': safe_is_occupied, 
        'msg': messages.current_message(safe_is_occupied),
    })
