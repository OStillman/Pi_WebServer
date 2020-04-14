from flask import Flask, render_template, request
import getJSON
import sys
import json

app = Flask(__name__)


@app.route('/')
def index():
    # data = {"apples": 7, "cheese": 1};
    data = getJSON.get_file()
    return render_template('index.html', data=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        data = request.get_json(force=True)
        #data = request.data
        is_there = getJSON.add_to_file(data)
        if is_there:
            return json.dumps({'success':False}), 400, {'ContentType':'application/json'} 
        else:
            return json.dumps({'success':True}), 201, {'ContentType':'application/json'} 




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
