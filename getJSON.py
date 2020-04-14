import json

def get_file():
    result = None
    with open('static/json/options.json') as f:
        result = json.loads(f.read())
    # print(result.days.day[0].alarm_time)
    return result

def add_to_file(appendMe):
    file_contents = get_file()
    file_contents['menu']['options'].append(appendMe)
    with open("static/json/options.json", "w") as file:
        file.write(json.dumps(file_contents, indent=4))
