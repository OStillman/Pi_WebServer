import getJSON
import datetime
import sys

class DayFetch():
    def __init__(self, shows=None):
        end_data = {"planner": {"shows": []}}
        data = getJSON.get_file("shows")
        today = self.getDayNum()
        day_links = data['planner']['days'][today]['shows']
        end_data = self.getShows(data, day_links, end_data)
        # print(str(end_data), file=sys.stderr)
        end_data = self.sortShows(end_data)
        self._shows = end_data
        # self._shows = self.getDayNum()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    def getDayNum(self):
        return datetime.datetime.today().weekday()

    def getShows(self, full_data, show_ids, end_data):
        for show_id in show_ids:
            end_data['planner']['shows'].append(full_data['planner']['shows'][show_id])
        return end_data

    def sortShows(self, full_data):
        sorted_data = {"planner": {"19": [], "20": [], "21": [], "22": []}}
        for show in full_data['planner']['shows']:
            if "19" in show['time']:
                sorted_data['planner']['19'].append(show)
            elif "20" in show['time']:
                sorted_data['planner']['20'].append(show)
            elif "21" in show['time']:
                sorted_data['planner']['21'].append(show)
            elif "22" in show['time']:
                sorted_data['planner']['22'].append(show)
        # print(sorted_data, file=sys.stderr)
        return sorted_data
