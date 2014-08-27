from flask import Flask, render_template
from multiprocessing import Value
import webserver

@webserver.app.route("/")
def home():
    return render_template('home.html', occupied=webserver.occstate.value)
