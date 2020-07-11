import urllib.request as request
import urllib.parse as parse
import json
import time

from tests import test_show_data as test_data


class SearchShow():
    def __init__(self, service, offset=0):
        '''
        Setup our URL for searching the shows
        @Param service = Service Number according to Freesat
        @Param Offset = Offset from today, default is 0, we allow up to 7
        '''
        self.url = "https://www.freesat.co.uk/tv-guide/api/{}/?channel={}".format(offset, service)
        self.offset = offset

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, offset):
        '''
        We need to allow the offset to be changed so we can keep the 1 instance of this class and check other days for the show
        '''
        self._offset = offset

    def fetch(self, test=False):
        '''
        Fetch the listing data for the current offset and channel
        @Param test = Boolean. Test data allows us to not have to test the API works...
        '''
        if not test:
            req = request.Request(url=self.url, method='GET')
            request.urlopen(req)
            # We need to format the response so it's usable
            print(request.urlopen(req).read().decode('utf-8'))
            self.show_data = json.loads(request.urlopen(req).read().decode('utf-8'))
        else:
            if self.offset == 0:
                self.show_data = test_data.data1
            else:
                self.show_data = test_data.data2

    def check_offset(self):
        '''
        We only allow the 7 day offset, if it's beyond that we won't continue
        '''
        if (self.offset > 7):
            return False
        else:
            return True
        
    def search(self, supplied_name):
        '''
        The main method used for this class
        @Param supplied_name = Show we are searching for
        Remember, we have already supplied the offset and service
        '''
        listing = []
        # Check the offset is 7 or less days
        if (self.check_offset()):
            # Fetch our data
            self.fetch(test=True)
            # Loop through each "event" i.e. show for that day
            for show in self.show_data[0]['event']:
                # Let's check if the show matches the name we've supplied
                if self.checkMatch(show["name"], supplied_name):
                    # If so, let's append the show info we need
                    listing.append(self.pullOutInfo(show))
            if len(listing) == 0:
                # Of course, if listing at this stage is empty, we'll need to return an error
                listing.append(["Error, show not found", self.offset])
        else:
            # The offset is past 7 so let's return an error
            listing.append(["Error, further than 7 days", self.offset])
        # Return our array - error or not
        return listing

    def checkMatch(self, show_name, supplied_name):
        '''
        We are going to check if the show contains the text searched for, easier this way as shows have long names
        @Param show_name = Show name from the API
        @Param supplied_name = Name supplied by the user for the show
        '''
        if supplied_name.lower() in show_name.lower():
            return True
        else:
            return False

    def pullOutInfo(self, matched_show):
        '''
        Simple method to pull out the info from the show that we have confirmed matches
        @Param matched_show = show object of the show matching the search term
        Returns the data for the user to view and evtId for us to use for validation and progress updates
        '''
        return [self.fixDateTime(matched_show["startTime"]), matched_show['evtId']]


    def fixDateTime(self, epoch):
        '''
        The time is currently in epoch, which is fine but to show to the user it'll be better for it to be in readable format
        @Param epoch = epoch of the show
        '''
        return time.strftime('%A %B %d, %Y %H:%M:%S', time.localtime(epoch))

