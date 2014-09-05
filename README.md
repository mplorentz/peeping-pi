peeping-pi
==========

An occupancy sensor built with Raspberry Pi

## Setup

1. Install [virtualenv](https://virtualenv.pypa.io/en/latest/virtualenv.html#installation) and [Python 3](https://www.python.org/downloads/) or greater.
2. Check out peeping-pi 
    git clone https://github.com/mplorentz/peeping-pi.git && cd peeping-pi
3. Make a new virtual environment and install dependencies
    virtualenv venv
    pip install -r requirements.txt
4. Start it up (must be run as root to access GPIO pins)
    sudo python peeping-pi.py

## Configuration

The webserver runs on port 80 by default. To change this, set the evironment variable `PEEPING_PI_PORT` to your desired port.

To change the GPIO pin that is read by sensor.py you can set the `PEEPING_PI_PIN` environment variable. Peeping Pi uses the Broadcom numbering system for the GPIO pins.
