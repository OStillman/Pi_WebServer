from os import path
import sys
import unittest
import json

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Shows import todayOutput

class test_Output(unittest.TestCase):

    def test_correct_output(self):
        TodayOutput = todayOutput.TodayOutput()
        data = {
        "planner": {
            "19": [
                {
                "channel": "BBC1",
                "duration": 60,
                "name": "Celebrity Masterchef",
                "time": "19:30"
                }
            ],
            "20": [
            {
                "channel": "BBC1",
                "duration": 30,
                "name": "Celebrity Masterchef",
                "time": "20:30"
                }
            ],
            "21": [
            {
                "channel": "BBC1",
                "duration": 30,
                "name": "The Other One",
                "time": "21:00"
            }
            ],
            "22": []
        }
        }
        assert TodayOutput.today == data

if __name__ == '__main__':
    unittest.main(verbosity=1)