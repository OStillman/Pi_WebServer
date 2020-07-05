import sqlite3

class AddLiveShow():
    def __init__(self, show_info):
        self.show_info = show_info
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def fetchChannelID(self):
        this_channel = int(self.show_info["channel"])
        print(this_channel)
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

class UpdateLiveShow():
    def __init__(self, id):
        self.id = id
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def updateDBES(self, ep, s):
        self.cursor.execute('''
        UPDATE LiveShows
        SET episodeNo = ?, seriesNo = ?
        WHERE id = ?;
        ''', (ep, s, self.id))
        self.db.commit()
        self.db.close()

    def updateDBInitialPassed(self):
        self.cursor.execute("""
        UPDATE LiveShows
        SET initialEpPassed = ?
        WHERE id = ?;
        """, ("Y", self.id))
        self.db.commit()
        self.db.close()


class FetchChannels:
    def __init__(self, channels=None, live_channels=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.db.close()

    def query(self):
        self.cursor.execute(''' SELECT *
        FROM channels;''')
        channels = []
        live_channels = []
        grid_row = 1
        for channel in self.cursor.fetchall():
            channels.append([channel[0], channel[1].lower(), grid_row, channel[2], channel[3]])
            if channel[0] % 2 == 0:
                grid_row = grid_row + 1
            if channel[2] == "Live":
                live_channels.append(channel[3])
        self._channels = channels
        self._live_channels = live_channels
        # self._tags = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels):
        self._channels = channels

    @property
    def live_channels(self):
        return self._live_channels

    @live_channels.setter
    def live_channels(self, live_channels):
        self._live_channels = live_channels

class FetchLiveShows():
    def __init__(self, service=None):
        self.service = service
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def liveshowsQuery(self):
        cursor = self.db.cursor()
        cursor.execute(''' 
        SELECT LiveShows.id, LiveShows.name, channel, duration, episodeNo, seriesNo, initialEvtid, initialEpPassed, channels.number
        from LiveShows
        INNER JOIN Channels ON LiveShows.channel = channels.id
        WHERE channels.number = ?; ''', (self.service, ))
        live_shows = cursor.fetchall()
        self.db.close()
        return live_shows

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = service