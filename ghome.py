import json
import db

class HandleRequest():
    def __init__(self, response=None):
        FetchToday = db.FetchToday()
        self.today = FetchToday.shows
        self.count = FetchToday.count
        self.simpleResponse()

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        self._response = response

    def formatShows(self, hour, spoken=False):
        these_shows = ""
        i = 0
        amount = len(self.today['planner'][hour])
        if amount > 0:
            for show in self.today['planner'][hour]:
                these_shows += show['name']
                i = i +1
                if i < amount:
                    these_shows += " and "
                else:
                    if spoken:
                        these_shows += "'s"
        else:
            these_shows = "N/A"
        return these_shows

    def formatShowSpeech(self):
        hour19 = self.formatShows("19", True)
        hour20 = self.formatShows("20", True)
        hour21 = self.formatShows("21", True)
        hour22 = self.formatShows("22", True)
        final_text = ""
        none = True
        if hour19 != "N/A":
            final_text += "{} on at 7. ".format(hour19)
            none = False
        if hour20 != "N/A":
            final_text += "{} on at 8. ".format(hour20)
            none = False
        if hour21 != "N/A":
            final_text += "{} on at 9. ".format(hour21)
            none = False
        if hour22 != "N/A":
            final_text += "{} on at 10. ".format(hour22)
            none = False
        if none:
            return "Watch something on demand or recorded!"
        else:
            return final_text
        

    def simpleResponse(self):
        self.response = json.dumps({
            "payload": {
                "google": {
                "expectUserResponse": False,
                "richResponse": {
                    "items": [
                    {
                        "simpleResponse": {
                        "textToSpeech": "Your schedule for tonight has {} shows...".format(self.count)
                        }
                    },
                    {
                        "basicCard": {
                        "title": "Your Schedule",
                        "formattedText": "__19:00:__ {}\n  \n __20:00:__ {}\n  \n __21:00:__ {}\n  \n__21:00:__ {}".format(
                            self.formatShows("19"),
                            self.formatShows("20"),
                            self.formatShows("21"),
                            self.formatShows("22")
                        ),
                        "image": {
                            "url": "https://storage.googleapis.com/actionsresources/logo_assistant_2x_64dp.png",
                            "accessibilityText": "Image alternate text"
                        },
                        "imageDisplayOptions": "CROPPED"
                        }
                    },
                    {
                        "simpleResponse": {
                        "textToSpeech": self.formatShowSpeech()
                        }
                    }
                    ]
                }
                }
            }
        })