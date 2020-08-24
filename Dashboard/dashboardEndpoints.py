from flask import render_template, request
import json
from flask import Blueprint

dashboard_endpoints = Blueprint('dashboard_endpoints', __name__)

@dashboard_endpoints.route('/')
def index():
    return render_template('dashboard/index.html')

@dashboard_endpoints.route('/tv')
def tv():
    return render_template('dashboard/tv.html')