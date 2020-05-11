import sqlite3
import sys
import datetime

class FetchToday:
    def __init__(self, shows=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.sortData()
        self._shows = self.sortData()
        self.db.close()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    def query(self):
        today = self.getDay() + 1
        #print (today, file=sys.stderr)
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
            #print(show, file=sys.stderr)
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

class FetchTVOD:
    def __init__(self, shows=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.ShowsQuery()
        self.AddRest()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    def ShowsQuery(self):
        #self.cursor.execute(''' ''')
        #self.shows = self.cursor.fetchall()
        #print(show1, file=sys.stderr)
        cursor = self.db.cursor()
        cursor.execute(''' SELECT Shows.id, Shows.name, Shows.time, Shows.duration, channels.name as channel
        FROM Shows
        INNER JOIN channels ON Shows.channel = channels.id; ''')
        self.all_shows = cursor.fetchall()

    def AddRest(self):
        end_data = {"Planner": {"Shows": []}}
        for show in self.all_shows:
            print(show, file=sys.stderr)
            this_show_id = show[0]
            this_show_tags = self.GetTags(this_show_id)
            this_show_days = self.GetDays(this_show_id)
            this_data = {"id": show[0], "name": show[1], "channel": show[4], "time": show[2], "duration": show[3], "days": this_show_days, "tags": this_show_tags}
            end_data["Planner"]["Shows"].append(this_data)
        self._shows = end_data

    def GetTags(self, show_id):
        tag_cursor = self.db.cursor()
        tag_cursor.execute('''SELECT tags.name
        FROM ShowTags
        INNER JOIN tags ON ShowTags.tag_id = tags.id
        WHERE ShowTags.show_id = ?;''', (show_id,))
        fetched_tags = tag_cursor.fetchall()
        tags = []
        for tag in fetched_tags:
            tags.append(tag[0])
        return tags

    def GetDays(self, show_id):
        day_cursor = self.db.cursor()
        day_cursor.execute('''SELECT days.name
        FROM ShowDays
        INNER JOIN days ON ShowDays.day_id = days.id
        WHERE ShowDays.show_id = ?;''', (show_id, ))
        fetched_days = day_cursor.fetchall()
        days = []
        for day in fetched_days:
            days.append(day[0])
        return days


