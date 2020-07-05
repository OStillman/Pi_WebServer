from Shows import db
from Shows import searchShows
import datetime


class OnTodayController():
    def __init__(self):
        self.channels = OnToday().getLiveChannels()
        self.fetchShows()

    def fetchShows(self):
        for channel in self.channels:
            shows = OnToday().fetchShows(channel)
            self.searchShows(shows)

    def searchShows(self, shows):
        for show in shows:
            show_list = OnToday().searchShows(show)
            print(show_list)


class OnToday():
    def __init__(self):
        self.FetchLiveShows = db.FetchLiveShows()
        self.FetchLiveChannels = db.FetchChannels()

    def getLiveChannels(self):
        return self.FetchLiveChannels.live_channels


    def fetchShows(self, service):
        '''
        Fetch all live shows stored in the DB
        '''
        self.FetchLiveShows.service = service
        shows_output = self.FetchLiveShows.liveshowsQuery()
        return(shows_output)

    def searchShows(self, show):
        '''
        Search the Show param is on today
        Offset = 0 as we only want to search today
        Show[8] = Show's service number (according to Freesat)
        '''
        # Set up the class instance
        SearchShows = searchShows.SearchShow(offset=0, service=show[8])
        # Search on the show name
        search_results = SearchShows.search(show[1])
        # Check the EnvtID is either one of the shows, or has already passed
        final_results = self.checkInitialEvtID(show, search_results)
        show_list = self.mergeResults(show, final_results)
        return show_list

    def checkInitialEvtID(self, show, results):
        '''
        We have initial eventID (Evtid) which is what the user has said "this is the first show"
        So, we need to check the show returned is, indeed, the first show they've said, or if the initial event has passed it can just be stored
        TODO: Check the Episode num or, failing that, the Series num is greater
        '''
        new_results = []
        show_evtid = show[6]
        initalevtpassed = show[7]
        for result in results:
            #print(result)
            # If the initial Event has not passed, we need to do check the Event ID from freesat is the one we aren interested in
            if initalevtpassed == "N":
                this_evtid = result[1]
                if this_evtid == show_evtid:
                    # Once we'ver found the initial event, we can store and allow any others to be added
                    #print("Found first eventid")
                    new_results.append(result)
                    initalevtpassed = "Y"
            else:
                # Initial event ID has passed so we can append all other results
                # TODO: Add the Series/Ep num check here
                #print("initial evtid passed")
                new_results.append(result)
        #print(new_results)
        return new_results

    def mergeResults(self, show, results):
        '''
        We need to prepare this to be added to the OnToday DB Table
        @Param results = [time, eventid]
        @Show = [LiveShows.id, LiveShows.name, channel, duration, episodeNo, seriesNo, initialEvtid, initialEpPassed, channels.number]
        Combine showID, epoch and eventID ready for storage
        TODO: Update DB with latest EpNo & SeriesNo
        '''
        #print(show[0])
        show_list = []
        for result in results:
            # Currently, the time is in a readable format, convert that back into an epoch timestamp - aids DB sorting later on
            this_epoch = datetime.datetime.strptime(result[0], '%A %B %d, %Y %H:%M:%S').timestamp()
            show_list.append([show[0], this_epoch, result[1]])
        #print(show_list)
        return show_list
        

