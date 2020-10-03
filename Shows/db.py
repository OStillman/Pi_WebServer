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

class AddODShow:
    def __init__(self, show_data):
        self.show_data = show_data
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

        self.InsertShow()
        self.show_id = self.cursor.lastrowid

        self.insertTags()

        self.db.commit()

        self.db.close()

        '''
        INSERT INTO ODShows(
            name,
            service,
        )
        values(
            "Test Show OD 2 - BBC",
            1
        );

        ID = 5


        INSERT INTO ShowTags(
            show_id,
            tag_id
        )
        values(
            5,
            3
        );
        '''

    def InsertShow(self):
        self.cursor.execute('''
            INSERT INTO ODShows(
            name,
            service
        )
        values(
            ?,
            ?
        );
        ''', (self.show_data['name'], self.show_data['service']))

    def insertTags(self):
        for tag in self.show_data['tags']:
            tag_id = self.checkTagExists(tag)
            self.cursor.execute('''
            INSERT INTO ShowTags(
                show_id,
                tag_id
            )
            VALUES(
                ?,
                ?
            )
            ''', (self.show_id, tag_id, ))
            

    def checkTagExists(self, tag):
        print(tag)
        select_cursor = self.db.cursor()
        select_cursor.execute('''
            SELECT * FROM tags
            WHERE name = ?;
            ''', (tag, ))
        try:
            return select_cursor.fetchall()[0][0]
        except IndexError:
            return self.addTag(tag)

    def addTag(self, tag):
        self.cursor.execute('''
        INSERT INTO tags(
            name
        )
        VALUES(
            ?
        )
        ''', (tag, ))
        return self.cursor.lastrowid

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

class FetchODShows():
    def __init__(self):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

    def odshowsQuery(self):
        cursor = self.db.cursor()
        cursor.execute(''' 
        SELECT ODShows.id, ODShows.name, channels.name, watching, episode, series
        FROM ODShows
        INNER JOIN Channels on ODShows.service = channels.id
        ORDER BY ODShows.watching DESC; ''')
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


class DeleteODShow():
    def __init__(self, id):
        self.id = id
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.deleteShow()
        self.db.commit()
        self.db.close()

    def deleteShow(self):
        self.cursor.execute('''DELETE FROM ODShows WHERE id = ?;''', (self.id,))
        self.cursor.execute('''DELETE FROM ShowTags WHERE show_id = ?;''', (self.id,))

class UpdateODProgress:
    def __init__(self, show):
        self.show = show
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

        self.query(show)

        self.db.commit()
        self.db.close()

    def query(self, show):
        self.cursor.execute('''
        UPDATE ODShows
        SET watching = ?, episode = ?, series = ?
        WHERE id = ?;
        ''', (show['watching'], show['episode'], show['series'], show['id'], ))


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

class ODShowTags():
    def __init__(self, show_id):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.show_id = show_id

    def showTagsQuery(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT tags.name
        FROM ShowTags
        INNER JOIN tags ON ShowTags.tag_id = tags.id
        WHERE ShowTags.show_id = ?;''', (self.show_id,))
        tags = cursor.fetchall()
        self.db.close()
        return tags 
