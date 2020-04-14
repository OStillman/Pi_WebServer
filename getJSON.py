import json
import sys

def get_file():
    result = None
    with open('static/json/options.json') as f:
        result = json.loads(f.read())
    # print(result.days.day[0].alarm_time)
    return result

def add_to_file(appendMe):
    file_contents = get_file()
    is_there = check_addition(appendMe, file_contents)
    if not is_there:
        file_contents['menu']['options'].append(appendMe)
        with open("static/json/options.json", "w") as file:
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

         
    
        
