from flask import Flask, render_template, request
import getJSON
import sys
import json
import db

import show_fetch

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
        data = getJSON.get_file("show_tags")
        return render_template('shows/add.html', data=data)
    else:
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        tags = False
        if len(data['tags']) > 0 or data['tags'] is not 'N/A':
            tags = True
        if getJSON.add_to_file(data, "shows", tags):
            return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
        else:
            return json.dumps({'success': False}), 500, {'ContentType': 'application/json'}

@app.route('/shows', methods=['GET', 'DELETE'])
def shows():
    if request.method == 'DELETE':
        data = request.get_json(force=True)
        getJSON.remove_show(int(data['element']), data['type'], "shows")
        return json.dumps({'success': True}), 204, {'ContentType': 'application/json'}
    else:
        # Get All data
        data = getJSON.get_file("shows")
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

        # Tags
        FetchTags = db.FetchTags()
        all_tags = FetchTags.tags

        print(all_shows, file=sys.stderr)
        print(today_shows, file=sys.stderr)
        print(all_tags, file=sys.stderr)



        return render_template('shows/index.html', all_shows=all_shows, today_shows=today_shows, tags=all_tags)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
