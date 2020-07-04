import sqlite3

class AddLiveShow():
    def __init__(self, show_info):
        self.show_info = show_info
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def fetchChannelID(self):
        this_channel = self.show_info["channel"]
        all_channels = FetchChannels().channels
        for channel in all_channels:
            if channel[4] == this_channel:
                return channel[0]

    def addToDB(self, channelID):
        self.cursor.execute('''
        INSERT INTO LiveShows(
            name, 
	        channel,  
	        duration, 
	        episodeNo,
	        seriesNo,
	        initialEvtid,
	        initialEpPassed
        )
        values(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        );
        ''', (self.show_info['name'], channelID, self.show_info['duration'], self.show_info['episodeNo'], self.show_info['seriesNo'], self.show_info['evtid'], "N"))
        self.db.commit()
        self.db.close()
        return True


class FetchChannels:
    def __init__(self, channels=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.db.close()

    def query(self):
        self.cursor.execute(''' SELECT *
        FROM channels;''')
        channels = []
        grid_row = 1
        for channel in self.cursor.fetchall():
            channels.append([channel[0], channel[1].lower(), grid_row, channel[2], channel[3]])
            if channel[0] % 2 == 0:
                grid_row = grid_row + 1
        self._channels = channels
        # self._tags = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels):
        self._channels = channels