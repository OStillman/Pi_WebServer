from tests import test_show_data as testData
import urllib.request as request
import urllib.parse as parse
import json

class AddShow():
    def __init__(self, evtid, channel):
        self.evtid = evtid
        self.channel = channel
        self.url = "https://www.freesat.co.uk/whats/showcase/api/channel/{}/episode/{}".format(self.channel, self.evtid)

    def show_details(self):
        all_show_data = self.fetchShowInfo(True)
        #print(all_show_data)
        show_info = self.formatData(all_show_data)
        #print(show_info)
        return show_info
        
    def fetchShowInfo(self, test=False):
        if not test:
            req = request.Request(url=self.url, method='GET')
            request.urlopen(req)
            #print(request.urlopen(req).read().decode('utf-8'))
            return json.loads(request.urlopen(req).read().decode('utf-8'))
        else:
            return testData.addData1

    def formatData(self, show):
        return {
            "evtid": self.evtid,
            "channel": self.channel,
            "duration": show["duration"],
            "seriesNo": show["seriesNo"],
            "episodeNo": show["episodeNo"],
            "name": show["name"]
            }