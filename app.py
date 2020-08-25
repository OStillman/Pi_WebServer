from flask import Flask, flash, redirect, url_for, render_template, request
from Shows.showsEndpoints import shows_endpoints
from Dashboard.dashboardEndpoints import dashboard_endpoints
from MQTT.mqtt_endpoints import mqtt_endpoints

import os
import blinkt

import getJSON
import sys
import json
import db
import door as door_actions
from Shows import dailyshow as ds
import ghome as assistant
from Photos import viewContents
from Photos import upload

import yaml

app = Flask(__name__)

app.register_blueprint(shows_endpoints, url_prefix='/shows')
app.register_blueprint(dashboard_endpoints, url_prefix='/dash')
app.register_blueprint(mqtt_endpoints, url_prefix='/mqtt')

@app.route('/meals')
def meals():
    # data = {"apples": 7, "cheese": 1};
    data = getJSON.get_file("meals")
    return render_template('meal_planner/index.html', data=data)


@app.route('/meals/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('meal_planner/add.html')
    else:
        data = request.get_json(force=True)
        #data = request.data
        is_there = getJSON.add_to_file(data, "meals")
        if is_there:
            return json.dumps({'success':False}), 400, {'ContentType':'application/json'} 
        else:
            return json.dumps({'success':True}), 201, {'ContentType':'application/json'}



@app.route('/Photos', defaults={'path': None}, methods=["GET", "POST"])
@app.route("/Photos/<path:path>")
def photos(path):
    if request.method == "GET":
        if not path:
            return renderDirectory(None)   
        else:
            path = "Photos/{}/".format(path)
            print(path)
            return renderDirectory(None, path)
    else:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        #file = request.files['file']
        all_photos = request.files.getlist("file")
        upload_succeeded = True
        photo_list = []
        for photo in all_photos:
            photo_list.append(photo.filename)
            if not upload.Upload(photo).tempStore():
                upload_succeeded = False
        if upload_succeeded:
            if upload.PictureActions(photo_list).processImages():
                return renderDirectory(True)
            else:
                return renderDirectory("Error")
        else:
            return renderDirectory(False)
        #if upload.Upload(file).tempStore():
            #upload.PictureActions(file.filename).completeUpload()
        #    return redirect(request.url)
        #else:
        #    return 'Nope'

def renderDirectory(upload_status, path=None):
    ViewContents = viewContents.ViewContents(path)
    contents = ViewContents.contents
    directory = ViewContents.location
    print(contents)
    return render_template('photos/index.html', contents=contents, directory=directory, upload_status=upload_status)

# Automation Routes

@app.route('/door', methods=['POST'])
def door():
    data = request.get_json(force=True)
    print(data, file=sys.stderr)
    door_actions.DoorSensor(data, loadYAML())
    return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}


@app.route('/dailyshow')
def dailyShow():
    ds.ActionDailyShows()
    return ('', 200)

@app.route('/ghome')
def ghome():
    HandleRequest = assistant.HandleRequest()
    return HandleRequest.response, 200, {'ContentType':'application/json'} 


def loadYAML():
    config_file = open(file='constants.yaml', mode='r')
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    config_file.close()
    return (config)

if __name__ == '__main__':
    config = loadYAML()
    if  config["Devmode"]["setting"]:
        blinkt.clear()
        blinkt.set_pixel(0, 255, 0, 0)
        blinkt.show()
    app.run(debug=True, host='0.0.0.0')
