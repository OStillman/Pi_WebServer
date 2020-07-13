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

class TodayShowOperations():
    def __init__(self):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
    
    def addTodayShow(self, details):
        self.cursor.execute("""
        INSERT INTO today(
	        showid,
	        epoch,
	        evtid,
            duration
        )
        values(
            ?,
            ?,
            ?,
            ?
        )
        """, (details[0], details[1], details[2], details[3]))
        self.db.commit()
        self.db.close()

    def retrieveTodayShows(self):
        self.cursor.execute(''' 
        SELECT LiveShows.name, channels.name, today.duration, epoch
        FROM today
        INNER JOIN Channels on LiveShows.channel = channels.id
        INNER JOIN LiveShows on today.showid = LiveShows.id
        ORDER BY epoch ASC;
        ''')
        todayShows = self.cursor.fetchall()
        self.db.close()
        return todayShows

    def deleteTodayShows(self):
        self.cursor.execute(''' 
        DELETE from today;
        ''')
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

class AllLiveShows():
    def __init__(self):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def liveshowsQuery(self):
        cursor = self.db.cursor()
        cursor.execute(''' 
        SELECT LiveShows.id, LiveShows.name, channel, duration, episodeNo, seriesNo, initialEvtid, initialEpPassed, channels.name
        from LiveShows
        INNER JOIN Channels ON LiveShows.channel = channels.id; ''')
        live_shows = cursor.fetchall()
        self.db.close()
        return live_shows


class DeleteLiveShow():
    def __init__(self, id):
        self.id = id
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.deleteShow()
        self.db.commit()
        self.db.close()

    def deleteShow(self):
        self.cursor.execute('''DELETE FROM LiveShows WHERE id = ?;''', (self.id,))
        self.cursor.execute('''DELETE FROM Today WHERE showid = ?;''', (self.id,))


class FetchTags:
    def __init__(self, tags=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.db.close()
        
    def query(self):
        self.cursor.execute(''' SELECT name
        FROM tags;''')
        tags = []
        for tag in self.cursor.fetchall():
            tags.append(tag[0])
        self._tags = tags
        # self._tags = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        self._tags = tags
