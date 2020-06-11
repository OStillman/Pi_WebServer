from flask import Flask, flash, redirect, url_for, render_template, request

import os
import blinkt

import getJSON
import sys
import json
import db
import door as door_actions
import dailyshow as ds
import ghome as assistant
from Photos import viewContents
from Photos import upload

import yaml

app = Flask(__name__)

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


@app.route('/shows/add', methods=['GET', 'POST'])
def add_shows():
    if request.method == 'GET':
        FetchTags = db.FetchTags()
        all_tags = FetchTags.tags

        # Channels
        FetchChannels = db.FetchChannels()
        all_channels = FetchChannels.channels

        print(all_channels, file=sys.stderr)
        
        #data = getJSON.get_file("show_tags")
        return render_template('shows/add.html', data=all_tags, channels=all_channels)
    else:
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        tags = False
        if len(data['tags']) > 0 or data['tags'] is not 'N/A':
            tags = True

        db.AddShow(data, tags)
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}

@app.route('/shows', methods=['GET', 'DELETE', 'PUT'])
def shows():
    if request.method == 'DELETE':
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        db.DeleteShows(int(data['element']))
        #getJSON.remove_show(int(data['element']), data['type'], "shows")
        return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}
    elif request.method == 'PUT':
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        db.UpdateProgress(data)
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        # Get All data
        #data = getJSON.get_file("shows")
        # Get shows on Today
        #shows_instance = show_fetch.DayFetch()
        #today_shows = shows_instance.shows  
        # Output
        #print(data, file=sys.stderr)

        #SQL Code

        # Today
        FetchToday = db.FetchToday()
        today_shows = FetchToday.shows

        # All
        FetchTVOD = db.FetchTVOD()
        all_shows = FetchTVOD.shows
        od_shows = FetchTVOD.od

        # Tags
        FetchTags = db.FetchTags()
        all_tags = FetchTags.tags

        print(all_shows, file=sys.stderr)
        print(today_shows, file=sys.stderr)
        print(all_tags, file=sys.stderr)
        print(od_shows, file=sys.stderr)



        return render_template('shows/index.html', all_shows=all_shows, today_shows=today_shows, tags=all_tags, od_shows=od_shows)

@app.route('/photos', defaults={'path': None}, methods=["GET", "POST"])
@app.route("/photos/<path:path>")
def photos(path):
    if request.method == "GET":
        if not path:
            return renderDirectory()   
        else:
            path = "Photos/{}/".format(path)
            print(path)
            return renderDirectory(path)
    else:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if upload.Upload(file).tempStore():
            return 'ok'
        else:
            return 'Nope'

def renderDirectory(path=None):
    ViewContents = viewContents.ViewContents(path)
    contents = ViewContents.contents
    directory = ViewContents.location
    print(contents)
    return render_template('photos/index.html', contents=contents, directory=directory)

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
