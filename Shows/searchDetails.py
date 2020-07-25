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
            print(self.url)
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
        data = {}
        try:
            data =  {
            "evtid": self.evtid,
            "channel": self.channel,
            "duration": show["duration"],
            "seriesNo": show["seriesNo"],
            "episodeNo": show["episodeNo"],
            "name": show["name"]
            }
        except KeyError:
            print("Can't find seriesNo, EpNo")
            attempted_fetch = self.attemptSeriesEpFetch(show["description"])
            if attempted_fetch[0] == True:
                data =  {
                "evtid": self.evtid,
                "channel": self.channel,
                "duration": show["duration"],
                "seriesNo": int(attempted_fetch[1]),
                "episodeNo": int(attempted_fetch[2]),
                "name": show["name"]
                }
        finally:
            return data

    def attemptSeriesEpFetch(self, description):
        '''split_description = description.split("(")[-1].split(")")[0]
        episode_fetch = split_description.split("Ep")[1]
        series_fetch = split_description.split("Ep")[0].split("S")[1].split(" ")[0]
        print(len(series_fetch))
        print(len(episode_fetch))
        if len(series_fetch) == 1 and len(episode_fetch) == 1:
            return [True, series_fetch, episode_fetch]
        else:
            return [False]'''

        ep_num = self.fetch_ep(description)
        print(ep_num)

        s_num = self.fetchSeries(description)
        print(s_num)

        if ep_num.isnumeric():
            print("EP is numeric")
            if s_num.isnumeric():
                # We can get away with not having a series, some shows only list their episode numbers
                print("Series numeric")
                return [True, int(s_num), int(ep_num)]
            else:
                print("No series, assuming S0")
                return [True, 0, int(ep_num)]
        else:
            return [False]


        

    def fetch_ep(self, description):
        '''
        Fetch the episode number from the description
        '''
        # Find the Char position of "Ep"
        find_point = description.find("Ep")
        print("=== Ep & Show search")
        print(find_point)
        # It'll give us the "E" part, so we need to then plus 2 to get the number
        num_point = find_point + 2
        is_numeric = True
        final_num = ""
        # -1 would indicate we couldn't find Ep in the description
        if find_point == -1:
            return False
        else:
            while is_numeric:
                # Check this is numeric
                if description[num_point].isnumeric():
                    # If so, we can add it to our description
                    final_num+= description[num_point]
                else:
                    # if it's not, we can stop the loop - we have our ep number
                    is_numeric = False
                # increase mnum_point for the next loop to look at the next char
                num_point+=1
            return final_num

    def fetchSeries(self, description, start=0):
        '''
        Fetch series, similar to fetch ep but has a few more complexities...
        @Param start = 0, can be used to set the "search from char" position for S's in the string elsewhere
        '''
        # Find the S, using the start char position
        find_series_point = description.find("S", start)
        print(find_series_point)
        # Only add 1 this time, S is only 1 char long
        num_point = find_series_point + 1
        is_numeric = True
        initially_numeric = False
        final_num = ""
        # Minus 1 indicates there's no sign of a S remaining i.e. series isn't in the desc
        if find_series_point == -1:
            return False
        else:
            while is_numeric:
                if description[num_point].isnumeric():
                    print("IS numeric")
                    print(description[num_point])
                    # Add this number
                    final_num = final_num + description[num_point]
                    # This does have numbers, so initally numeric allows us to return these numbers at the end
                    initially_numeric = True
                    num_point+=1
                else:
                    # Not numeric, we've (maybe) found the series
                    is_numeric = False
                print(final_num)
            # If it was initially numeric, we have a number, so this will be the series
            if initially_numeric:
                print(final_num)
                return final_num
            else:
                # We haven't found a number, it was initially numeric, re-call the function using the current char as the start search location
                return(self.fetchSeries(description, start=num_point))
                

        


        
