from os import path
import sys
import unittest
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Shows import addShows

class testAddShows(unittest.TestCase):

    def setUp(self):
        self.AddShow = addShows.AddShow()
        self.AddShow.details = {"name": "show1", "channel": "bbc1"}
    
    def test_takes_show(self):
        

if __name__ == '__main__':
    unittest.main(verbosity=1)