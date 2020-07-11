from tests import test_show_data as testData
import urllib.request as request
import urllib.parse as parse
import json

class SearchShowDetail():
    def __init__(self, evtid, channel):
        '''
        It's useful to get further information about the episode, which is what this class does
        @param evtid = Event ID for the selected show
        @param channel = The service according to freesat for this show
        '''
        self.evtid = evtid
        self.channel = channel
        self.url = "https://www.freesat.co.uk/whats/showcase/api/channel/{}/episode/{}".format(self.channel, self.evtid)

    def show_details(self):
        '''
        The main class for pulling out the show info
        '''
        # First let's fetch the show
        all_show_data = self.fetchShowInfo(test=False)
        #print(all_show_data)
        # Then let's format it so we only get the data we need/want
        show_info = self.formatData(all_show_data)
        #print(show_info)
        return show_info
        
    def fetchShowInfo(self, test=False):
        '''
        Fetch from the API using our URL formatted in the class instance
        @Param test = if test, some data about "The other one" can be used
        '''
        if not test:
            req = request.Request(url=self.url, method='GET')
            request.urlopen(req)
            #print(request.urlopen(req).read().decode('utf-8'))
            return json.loads(request.urlopen(req).read().decode('utf-8'))
        else:
            return testData.addData1

    def formatData(self, show):
        '''
        We don't need all the data, so let's pull out only the data we need
        @Param show = the show object pulled from the API
        '''
        return {
            "evtid": self.evtid,
            "channel": self.channel,
            "duration": show["duration"],
            "seriesNo": show["seriesNo"],
            "episodeNo": show["episodeNo"],
            "name": show["name"]
            }