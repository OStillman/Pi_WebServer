from flask import render_template, request
import json
from flask import Blueprint
from MQTT import presence

mqtt_endpoints = Blueprint('mqtt_endpoints', __name__)


@mqtt_endpoints.route('/owen/in')
def owenIn():
    print("Owen's In")
    OwenPresence = presence.Presence("owen", "in")
    OwenPresence.updateStatus()
    return "Ok"

@mqtt_endpoints.route('/owen/out')
def owenOut():
    print("Owen's Out")
    OwenPresence = presence.Presence("owen", "out")
    OwenPresence.updateStatus()
    return "Ok"