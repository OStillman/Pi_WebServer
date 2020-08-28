from flask import render_template, request
import json
from flask import Blueprint
from MQTT import presence

mqtt_endpoints = Blueprint('mqtt_endpoints', __name__)


@mqtt_endpoints.route('/presence', methods=["POST"])
def presence_ep():
    print("Received presence update")
    data = request.get_json(force=True)
    MemberPresence = presence.Presence(data["member"], data["status"])
    MemberPresence.updateStatus()
    return "Ok"