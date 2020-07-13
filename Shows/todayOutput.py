from Shows import db
import time

class TodayOutput():
    def __init__(self, today=None):
        self.TodayShowOperations = db.TodayShowOperations()
        self.shows = list(self.TodayShowOperations.retrieveTodayShows())
        self.fixDisplay()
        self.readyOutput()


    def fixDisplay(self):
        final_shows = []
        for show in self.shows:
            show = list(show)
            show[2] = self.fixDuration(show[2])
            show[3] = self.fixEpoch(show[3])
            final_shows.append(show)
        print(final_shows)
        self.shows = final_shows

    def readyOutput(self):
        sorted_data = {"planner": {"19": [], "20": [], "21": [], "22": []}}
        self.count = len(self.shows)
        for show in self.shows:
            #print(show, file=sys.stderr)
            this_data = {"name": show[0], "duration": show[2], "time": show[3], "channel": show[1]}
            time_string = str(show[3])
            if "19" in time_string:
                sorted_data['planner']['19'].append(this_data)
            elif "20" in time_string:
                sorted_data['planner']['20'].append(this_data)
            elif "21" in time_string:
                sorted_data['planner']['21'].append(this_data)
            elif "22" in time_string:
                sorted_data['planner']['22'].append(this_data)
        print(sorted_data)
        self.today = sorted_data


    def fixEpoch(self, epoch):
        return time.strftime('%H:%M', time.localtime(epoch))

    def fixDuration(self, duration):
        return int(duration) / 60
            

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self, today):
        self._today = today