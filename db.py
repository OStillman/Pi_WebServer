import sqlite3
import sys
import datetime

class FetchToday:
    def __init__(self, shows=None, count=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.sortData()
        self._shows = self.sortData()
        self.db.close()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    def query(self):
        today = self.getDay() + 1
        #print (today, file=sys.stderr)
        self.cursor.execute(''' SELECT Shows.name, Shows.duration, Shows.time, channels.name
        FROM Shows
        INNER JOIN ShowDays ON Shows.id = ShowDays.show_id
        INNER JOIN days ON ShowDays.day_id = days.id
        INNER JOIN channels ON Shows.channel = channels.id
        WHERE days.id = ?; ''', (today,))
        self.shows = self.cursor.fetchall()
        #print(show1, file=sys.stderr)

    def sortData(self):
        sorted_data = {"planner": {"19": [], "20": [], "21": [], "22": []}}
        self.count = len(self.shows)
        for show in self.shows:
            #print(show, file=sys.stderr)
            this_data = {"name": show[0], "duration": show[1], "time": show[2], "channel": show[3]}
            if "19" in show[2]:
                sorted_data['planner']['19'].append(this_data)
            elif "20" in show[2]:
                sorted_data['planner']['20'].append(this_data)
            elif "21" in show[2]:
                sorted_data['planner']['21'].append(this_data)
            elif "22" in show[2]:
                sorted_data['planner']['22'].append(this_data)
        return sorted_data

    def getDay(self):
        return datetime.datetime.today().weekday()

class FetchTVOD:
    def __init__(self, shows=None, od=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.ShowsQuery()
        self.AddRest()
        self.db.close()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, show):
        self._shows = show

    @property
    def od(self):
        return self._od

    @od.setter
    def od(self, od):
        self._od = od

    def ShowsQuery(self):
        #self.cursor.execute(''' ''')
        #self.shows = self.cursor.fetchall()
        #print(show1, file=sys.stderr)
        cursor = self.db.cursor()
        cursor.execute(''' SELECT Shows.id, Shows.name, Shows.time, Shows.duration, channels.name as channel, Shows.watching, Shows.series, Shows.episode
        FROM Shows
        INNER JOIN channels ON Shows.channel = channels.id
        ORDER BY Shows.watching DESC; ''')
        self.all_shows = cursor.fetchall()

    def AddRest(self):
        end_data = {"Planner": {"Shows": []}}
        for show in self.all_shows:
            print(show, file=sys.stderr)
            this_show_id = show[0]
            this_show_tags = self.GetTags(this_show_id)
            this_show_days = self.GetDays(this_show_id)
            this_data = {
                "id": show[0], 
                "name": show[1], 
                "channel": show[4], 
                "time": show[2], 
                "duration": show[3], 
                "days": this_show_days, 
                "tags": this_show_tags,
                "watching": show[5],
                "series": show[6],
                "episode": show[7]
            }
            end_data["Planner"]["Shows"].append(this_data)
        self._shows = end_data
        self.ODShows(end_data)

    def ODShows(self, end_data):
        od_data = {"Planner": {"Shows": []}}
        for show in end_data['Planner']['Shows']:
            show_channel = show['channel']
            show_days = show["days"]
            if "N/A" in show_days:
                od_data['Planner']['Shows'].append(show)
            elif "Sky" in show_channel:
                od_data['Planner']['Shows'].append(show)
            elif "Amazon" in show_channel:
                od_data['Planner']['Shows'].append(show)
            elif "Netflix" in show_channel:
                od_data['Planner']['Shows'].append(show)
            elif "Disney" in show_channel:
                od_data['Planner']['Shows'].append(show)
        self._od = od_data



    def GetTags(self, show_id):
        tag_cursor = self.db.cursor()
        tag_cursor.execute('''SELECT tags.name
        FROM ShowTags
        INNER JOIN tags ON ShowTags.tag_id = tags.id
        WHERE ShowTags.show_id = ?;''', (show_id,))
        fetched_tags = tag_cursor.fetchall()
        tags = []
        for tag in fetched_tags:
            tags.append(tag[0])
        return tags

    def GetDays(self, show_id):
        day_cursor = self.db.cursor()
        day_cursor.execute('''SELECT days.name
        FROM ShowDays
        INNER JOIN days ON ShowDays.day_id = days.id
        WHERE ShowDays.show_id = ?;''', (show_id, ))
        fetched_days = day_cursor.fetchall()
        days = []
        if fetched_days:
            for day in fetched_days:
                days.append(day[0])
        else:
            days.append("N/A")
        return days

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
            channels.append([channel[0], channel[1].lower(), grid_row, channel[2]])
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

class FetchOD:
    def __init__(self, shows=None):
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.query()
        self.db.close()

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, shows):
        self._shows = shows

    def query(self):
        self.cursor.execute('''SELECT Shows.name, Shows.duration, channels.name, days.name, Shows.watching
        FROM Shows
        INNER JOIN ShowDays ON Shows.id = ShowDays.show_id
        INNER JOIN days ON ShowDays.day_id = days.id
        INNER JOIN channels ON Shows.channel = channels.id
        WHERE channels.id IN (8,9,10,11) OR days.name = "N/A"
        ORDER BY Shows.watching DESC;''')
        # end_data = {"Planner": {"Shows": []}}
        shows = {"Planner": {"ODShows": []}}
        for show in self.cursor.fetchall():
            print(show, file=sys.stderr)
            shows['Planner']['ODShows'].append({"name": show[0], "duration": show[1], "service": show[2], "day": show[3]})
        #print(shows, file=sys.stderr)
        self._shows = shows

class DeleteShows:
    def __init__(self, id):
        self.id = id
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()
        self.deleteShow()
        self.db.commit()
        self.db.close()

    def deleteShow(self):
        self.cursor.execute('''DELETE FROM Shows WHERE id = ?;''', (self.id,))
        self.cursor.execute('''DELETE FROM ShowDays WHERE show_id = ?;''', (self.id,))
        self.cursor.execute('''DELETE FROM ShowTags WHERE show_id = ?;''', (self.id,))


class AddShow:
    def __init__(self, show_data, new_tags):
        self.show_data = show_data
        self.new_tags = new_tags
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

        self.InsertShow()
        self.show_id = self.cursor.lastrowid

        self.insertDays()

        self.insertTags()

        self.db.commit()

        self.db.close()

        '''
        INSERT INTO Shows(
            name,
            channel,
            time,
            duration
        )
        values(
            "Test Show OD 2 - BBC",
            1,
            "N/A",
            "01:00"
        );

        ID = 5

        INSERT INTO ShowDays(
            show_id,
            day_id
        )
        values(
            5,
            8
        );

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
            INSERT INTO Shows(
            name,
            channel,
            time,
            duration
        )
        values(
            ?,
            ?,
            ?,
            ?
        );
        ''', (self.show_data['name'], self.show_data['service'], self.show_data['time'], self.show_data['duration']))

    def insertDays(self):
        if not self.show_data['days'] == "N/A":
            for day in self.show_data['days']:
                #print(day, file=sys.stderr)
                self.cursor.execute('''
                INSERT INTO ShowDays(
                    show_id,
                    day_id
                )
                values(
                    ?,
                    ?
                );
                ''', (self.show_id, day))

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
        print(tag, file=sys.stderr)
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


class UpdateProgress:
    def __init__(self, show):
        self.show = show
        self.db = sqlite3.connect('DB/webserver.db')
        self.cursor = self.db.cursor()

        self.query(show)

        self.db.commit()
        self.db.close()

    def query(self, show):
        self.cursor.execute('''
        UPDATE Shows
        SET watching = ?, episode = ?, series = ?
        WHERE id = ?;
        ''', (show['watching'], show['episode'], show['series'], show['id'], ))
