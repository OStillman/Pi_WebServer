import urllib.request as request
import urllib.parse as parse
import json
import time

from tests import test_show_data as test_data


class SearchShow():
    def __init__(self, service, offset=0):
        self.url = "https://www.freesat.co.uk/tv-guide/api/{}/?channel={}".format(offset, service)
        self.offset = offset

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        self._offset = offset

    def fetch(self, test=False):
        if not test:
            req = request.Request(url=self.url, method='GET')
            request.urlopen(req)
            print(request.urlopen(req).read().decode('utf-8'))
            self.show_data = json.loads(request.urlopen(req).read().decode('utf-8'))
        else:
            if self.offset == 0:
                self.show_data = test_data.data1
            else:
                self.show_data = test_data.data2

    def check_offset(self):
        if (self.offset > 7):
            return False
        else:
            return True
        
    def search(self, supplied_name):
        listing = []

        if (self.check_offset()):
            self.fetch(test=True)
            for show in self.show_data[0]['event']:
                if self.checkMatch(show["name"], supplied_name):
                    listing.append(self.pullOutInfo(show))
            if len(listing) == 0:
                listing.append(["Error, show not found", self.offset])
        else:
            listing.append(["Error, further than 7 days", self.offset])
        return listing

    def checkMatch(self, show_name, supplied_name):
        if supplied_name.lower() in show_name.lower():
            return True
        else:
            return False

    def pullOutInfo(self, matched_show):
        return [self.fixDateTime(matched_show["startTime"]), matched_show['evtId']]


    def fixDateTime(self, epoch):
        return time.strftime('%A %B %d, %Y %H:%M:%S', time.localtime(epoch))

