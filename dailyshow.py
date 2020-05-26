import db
import notify

class ActionDailyShows:
    def __init__(self):
        FetchToday = db.FetchToday()
        self.today_shows = FetchToday.shows
        self.formatText()
        notify.Notify("Daily Show Digest", self.notif_desc)

    def formatText(self):
        end_data = ""
        print(self.today_shows)
        end_data+=self.formatHour("19:00", self.today_shows['planner']['19'])
        end_data+=self.formatHour("20:00", self.today_shows['planner']['20'])
        end_data+=self.formatHour("21:00", self.today_shows['planner']['21'])
        end_data+=self.formatHour("22:00", self.today_shows['planner']['22'])
        print(end_data)
        self.notif_desc = end_data

    def formatHour(self, this_hour, this_hour_data):
        formatted = "{}\n".format(this_hour)
        for show in this_hour_data:
            print(show)
            formatted+="    - {} - {}\n".format(show['name'], show['duration'])
        return formatted
