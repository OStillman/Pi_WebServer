import json
import sys
import random

def get_file(application):
    file = getFileLocation(application)
    result = None
    with open(file) as f:
        result = json.loads(f.read())
    # print(result.days.day[0].alarm_time)
    return fileContents(result, application)


def getFileLocation(application):
    if application == "meals":
        file = 'static/meal_planner/json/options.json'
    else:
        file = 'static/shows/json/planner.json'
    return file

def fileContents(file, application):
    if application == "meals":
        random.shuffle(file['menu']['options'])
    elif application == "show_tags":
        file = file['planner']['tags']
    return file


def add_to_file(appendMe, application, tags=False):
    if application == "meals":
        file = 'static/meal_planner/json/options.json'
        return add_meals(appendMe, file, application)
    else:
        file = 'static/shows/json/planner.json'
        return add_show(appendMe, file, application, tags)


def add_show(appendMe, file, application, tags):
    file_contents = get_file(application)
    new_tags = appendMe['new_tags']
    del appendMe['new_tags']
    if appendMe['days'] == "N/A":
        del appendMe['days']
        del appendMe['time']
        file_contents['planner']['OD'].append(appendMe)
    else:
        this_day = appendMe['days'][0]
        this_position = len(file_contents['planner']['shows'])
        file_contents['planner']['shows'].append(appendMe)
        file_contents['planner']['days'][this_day]['shows'].append(this_position)
    print(new_tags, file=sys.stderr)
    if tags:
        for tag in new_tags:
            file_contents['planner']['tags'].append(tag)
    with open(file, "w") as file:
        file.write(json.dumps(file_contents, indent=4))
    return True


def remove_show(element_num, remove_type, application):
    file_contents = get_file(application)
    if (remove_type == "tv"):
        # this_day = file_contents['planner']['shows'][element_num]['days'][0]
        # file_contents['planner']['days'][this_day]['shows'].remove(element_num)
        del file_contents['planner']['shows'][element_num]
        file_contents = remove_number_bump(file_contents)
    else:
        del file_contents['planner']['OD'][element_num]
    with open('static/shows/json/planner.json', "w") as file:
        file.write(json.dumps(file_contents, indent=4))
    return True

def remove_number_bump(file_contents):
    # Remove all day shows
    # Go through all shows, get their day and add
    file_contents['planner']['days'][0]['shows'] = []
    file_contents['planner']['days'][1]['shows'] = []
    file_contents['planner']['days'][2]['shows'] = []
    file_contents['planner']['days'][3]['shows'] = []
    file_contents['planner']['days'][4]['shows'] = []
    file_contents['planner']['days'][5]['shows'] = []
    file_contents['planner']['days'][6]['shows'] = []
    this_id = 0
    for show in file_contents['planner']['shows']:
        print(show, file=sys.stderr)
        this_day = show['days'][0]
        file_contents['planner']['days'][this_day]['shows'].append(this_id)
        this_id = this_id + 1
    return file_contents


def add_meals(appendMe, file, application):
    file_contents = get_file(application)
    is_there = check_addition(appendMe, file_contents)
    if not is_there:
        file_contents['menu']['options'].append(appendMe)
        with open(file, "w") as file:
            file.write(json.dumps(file_contents, indent=4))
    return is_there


def check_addition(new_item, file_contents):
    # TODO: Check the Item isn't already there
    # Get total options, run through checking the title against the input
    # If not there, we can add it in
    is_there = False
    new_option = new_item['name'].lower()
    for option in file_contents['menu']['options']:
         print(option['name'], file=sys.stderr)
         this_option = option['name'].lower()
         if  new_option in this_option:
             print("It's already there!", file=sys.stderr)
             is_there = True
    return is_there

         
    
        
