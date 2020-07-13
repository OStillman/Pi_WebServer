from Shows import todayOutput
import notify

class ActionDailyShows:
    def __init__(self):
        FetchToday = todayOutput.TodayOutput()
        self.today_shows = FetchToday.today
        self.formatText()
        notify.Notify("Daily Show Digest", self.notif_desc)

    def formatText(self):
        end_data = ""
        print(self.today_shows)
        end_data+=self.formatDisplay(self.today_shows['planner']['19'])
        end_data+=self.formatDisplay(self.today_shows['planner']['20'])
        end_data+=self.formatDisplay(self.today_shows['planner']['21'])
        end_data+=self.formatDisplay(self.today_shows['planner']['22'])
        print(end_data)
        if len(end_data) > 0:
            self.notif_desc = "On Tonight:{}".format(end_data[:-1])
        else:
            self.notif_desc = "FYI, you have no shows on tonight!"
        
    def formatDisplay(self, this_hour_data):
        formatted = ""
        for show in this_hour_data:
            print(show)
            formatted+=" {},".format(show['name'])
        return formatted