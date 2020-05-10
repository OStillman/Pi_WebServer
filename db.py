import sqlite3
import sys

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
        #TODO Add in today's date in select statement
        self.cursor.execute(''' SELECT s.name, s.time, ch.name, s.duration
        FROM Shows s, channels ch
        JOIN Shows ON s.channel = ch.id
        WHERE s.channel = 1; ''')
        self.shows = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    def sortData(self):
        sorted_data = {"planner": {"19": [], "20": [], "21": [], "22": []}}
        for show in self.shows:
            print(show, file=sys.stderr)
            this_data = {"name": show[0], "time": show[1], "channel": show[2], "duration": show[3]}
            if "19" in show[1]:
                sorted_data['planner']['19'].append(this_data)
            elif "20" in show[1]:
                sorted_data['planner']['20'].append(this_data)
            elif "21" in show[1]:
                sorted_data['planner']['21'].append(this_data)
            elif "22" in show[1]:
                sorted_data['planner']['22'].append(this_data)
        return sorted_data


        '''for show in full_data['planner']['shows']:
            if "19" in show['time']:
                sorted_data['planner']['19'].append(show)
            elif "20" in show['time']:
                #sorted_data['planner']['20'] = self.checkOrder(sorted_data['planner']['20'], show)
                sorted_data['planner']['20'].append(show)
            elif "21" in show['time']:
                sorted_data['planner']['21'].append(show)
            elif "22" in show['time']:
                sorted_data['planner']['22'].append(show)
        # print(sorted_data, file=sys.stderr)
        return sorted_data'''

