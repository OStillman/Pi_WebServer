from os import path
import sys
import unittest
from unittest import mock
import json

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Shows import searchShows

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


    

        

if __name__ == '__main__':
    unittest.main(verbosity=1)