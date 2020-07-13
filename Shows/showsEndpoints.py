from flask import render_template, request
import json
from flask import Blueprint
import sys

import db
from Shows import todayOutput
from Shows import allShows
from Shows import searchDetails
from Shows import searchShows
from Shows import db as ShowsDB
from Shows import onToday

shows_endpoints = Blueprint('shows_endpoints', __name__)

#Legacy - TODO: Pull out rest of DB queries and, of course, the OD stuff
@shows_endpoints.route('/add', methods=['GET', 'POST'])
def add_shows():
    if request.method == 'GET':
        FetchTags = ShowsDB.FetchTags()
        all_tags = FetchTags.tags

        # Channels
        FetchChannels = ShowsDB.FetchChannels()
        all_channels = FetchChannels.channels

        print(all_channels, file=sys.stderr)
        
        #data = getJSON.get_file("show_tags")
        return render_template('shows/add.html', data=all_tags, channels=all_channels)
    else:
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        '''tags = False
        if len(data['tags']) > 0 or data['tags'] is not 'N/A':
            tags = True

        db.AddShow(data, tags)'''
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}

@shows_endpoints.route('/live/search', methods=['POST'])
def showsSearch():
    data = request.get_json(force=True)
    print(data, file=sys.stderr)
    SearchShow = searchShows.SearchShow(data['service'], data['offset'])
    show_times = SearchShow.search(data['title'])
    print(show_times)
    return json.dumps(show_times), 200, {'ContentType': 'application/json'}

@shows_endpoints.route('/live', methods=['POST', 'DELETE'])
def liveAdd():
    if request.method == "POST":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        success = True
        try:
            found_show = searchDetails.SearchShowDetail(data["evtid"], data["service"]).show_details()
            AddLiveShow = ShowsDB.AddLiveShow(found_show)
            channel_id = AddLiveShow.fetchChannelID()
            AddLiveShow.addToDB(channel_id)
            print(found_show)
        except KeyError:
            success = False
        finally:
            if success:
                return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
            else:
                return json.dumps({'success': False}), 400, {'ContentType': 'application/json'}
    elif request.method == "DELETE":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        ShowsDB.DeleteLiveShow(int(data['element']))
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}


@shows_endpoints.route('/live/today')
def showsLiveToday():
    onToday.OnTodayController()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Legacy TODO: Remove dependancy here on DELTE and PUT, move out/sort OD parts
@shows_endpoints.route('/', methods=['GET', 'DELETE', 'PUT'])
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
        #FetchToday = db.FetchToday()
        #today_shows = FetchToday.shows
        TodayOutput = todayOutput.TodayOutput()
        today_shows = TodayOutput.today


        # All
        FetchTVOD = db.FetchTVOD()
        all_shows = FetchTVOD.shows
        od_shows = FetchTVOD.od

        #NewAll - Live
        all_live_shows = allShows.GetAllLiveShows().retrieveShows()

        # Tags
        FetchTags = ShowsDB.FetchTags()
        all_tags = FetchTags.tags

        print(all_shows, file=sys.stderr)
        print(today_shows, file=sys.stderr)
        print(all_tags, file=sys.stderr)
        print(od_shows, file=sys.stderr)



        return render_template('shows/index.html', all_shows=all_shows, live_shows=all_live_shows, today_shows=today_shows, tags=all_tags, od_shows=od_shows)
