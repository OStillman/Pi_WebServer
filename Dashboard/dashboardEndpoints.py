from flask import render_template, request
import json
from flask import Blueprint

from MQTT import presence
from MQTT import shows

dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)

@dashboard_endpoints.route('/')
def index():
    return render_template('dashboard/index.html')

@dashboard_endpoints.route('/tv')
def tv():
    return render_template('dashboard/tv.html')

@dashboard_endpoints.route('/initial')
def initialPresence():
    PresenceLoad = presence.Presence(None, None)
    PresenceLoad.fetchStatus()
    TodayShows = shows.ShowsToday()
    today = TodayShows.fetchToday()
    return "Ok"