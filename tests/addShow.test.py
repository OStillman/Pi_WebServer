from os import path
import sys
import unittest
from unittest import mock
import json

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Shows import searchShows
from Shows import searchDetails
from Shows import db

class testSearchShow(unittest.TestCase):

    def setUp(self):
        self.details = {"name": "Masterchef", "service": "512"}
        self.SearchShow = searchShows.SearchShow(512)

    def test_finds_show(self):
        show_times = self.SearchShow.search("Masterchef")
        assert show_times[0] == ['Friday July 03, 2020 19:30:00', 13116]

    def test_show_not_found(self):
        show_times = self.SearchShow.search("Notathing")
        assert show_times[0] == ["Error, show not found", 0]
    
    def test_show_can_be_found(self):
        show_times = self.SearchShow.search("Different Show")
        assert show_times[0] == ["Error, show not found", 0]
        self.SearchShow.offset = self.SearchShow.offset + 1
        show_times = self.SearchShow.search("Different Show")
        assert show_times[0] == ['Friday July 03, 2020 16:30:00', 13474]

    def test_no_over_7(self):
        self.SearchShow.offset = 8
        show_times = self.SearchShow.search("Different Show")
        assert show_times[0] == ['Error, further than 7 days', 8]


class testAddShow(unittest.TestCase):

    def test_show_found(self):
        found_show = searchDetails.SearchShowDetail(13118, 512).show_details()
        assert found_show['evtid'] == 13118
        assert found_show['name'] == "The Other One"
        assert found_show['duration'] == 1800
        assert found_show['seriesNo'] == 2
        assert found_show['episodeNo'] == 5

    def test_correct_channel(self):
        found_show = {
            "evtid": 13118,
            "channel": 512,
            "duration": 1800,
            "seriesNo": 2,
            "episodeNo": 5,
            "name": "The Other One"
            }
        channel_id = db.AddLiveShow(found_show).fetchChannelID()
        assert channel_id == 1

    def test_add_to_DB(self):
        found_show = {
            "evtid": 13118,
            "channel": 512,
            "duration": 1800,
            "seriesNo": 2,
            "episodeNo": 5,
            "name": "The Other One"
            }
        AddLiveShow = db.AddLiveShow(found_show)
        channel_id = AddLiveShow.fetchChannelID()
        added = AddLiveShow.addToDB(channel_id)
        assert added == True







    

        

if __name__ == '__main__':
    unittest.main(verbosity=1)