import sqlite3
import sys
import datetime

class FetchToday:
    def __init__(self, shows=None):
        db = sqlite3.connect('DB/webserver.db')
        self.db = db
        self.cursor = self.db.cursor()
        self.query()
        self.sortData()
        self._shows = self.sortData()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    def query(self):
        today = self.getDay() + 1
        print (today, file=sys.stderr)
        #TODO Add in today's date in select statement
        self.cursor.execute(''' SELECT Shows.name, Shows.duration, Shows.time, channels.name
        FROM Shows
        INNER JOIN ShowDays ON Shows.id = ShowDays.show_id
        INNER JOIN days ON ShowDays.day_id = days.id
        INNER JOIN channels ON Shows.channel = channels.id
        WHERE days.id = ?; ''', (today,))
        self.shows = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    def sortData(self):
        sorted_data = {"planner": {"19": [], "20": [], "21": [], "22": []}}
        for show in self.shows:
            print(show, file=sys.stderr)
            this_data = {"name": show[0], "duration": show[1], "time": show[2], "channel": show[3]}
            if "19" in show[2]:
                sorted_data['planner']['19'].append(this_data)
            elif "20" in show[2]:
                sorted_data['planner']['20'].append(this_data)
            elif "21" in show[2]:
                sorted_data['planner']['21'].append(this_data)
            elif "22" in show[2]:
                sorted_data['planner']['22'].append(this_data)
        return sorted_data

    def getDay(self):
        return datetime.datetime.today().weekday()
