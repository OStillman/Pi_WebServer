from os import path
import sys
import unittest

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Shows import onToday

"""

class TestLiveChannelFetch(unittest.TestCase):

    def test_correct_number(self):
        livechannels = onToday.OnToday().getLiveChannels()
        assert len(livechannels) == 7
        assert livechannels == [512, 700, 1008, 1100, 1502, 1547, 1510]

    def test_correct_shows(self):
        live_shows = onToday.OnToday().fetchShows(512)
        assert live_shows[0][1] == "Celebrity Masterchef"
        assert live_shows[1][1] == "The Other One"

    def test_is_on_today(self):
        data = ["1", "Celebrity Masterchef", "", "", "", "", 13116, "N", 512]
        results = onToday.OnToday().searchShows(data)
        assert results == [['1', 1593801000.0, 13116], ['1', 1593804600.0, 13117]]

    def test_not_on_today(self):
        data = ["1", "Not On Today", "", "", "", "", 123456, "N", 512]
        results = onToday.OnToday().searchShows(data)
        assert results == []

"""

class TestControlFlow(unittest.TestCase):

    def test_flow(self):
        onToday.OnTodayController()
        assert 1 == 2

if __name__ == '__main__':
    unittest.main(verbosity=1)