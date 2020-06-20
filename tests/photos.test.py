import unittest
import sys
from os import path
import os

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Photos import upload

"""
class File_Location(unittest.TestCase):

    def setUp(self):
        self.PictureActions = upload.PictureActions("test.jpg")

    def test_correct_taken_time(self):
        taken_time = self.PictureActions.getDT()
        print(taken_time)
        assert "2020:06:11 15:51:11" in taken_time

    def test_correct_month(self):
        month = self.PictureActions.getMonth("2020:06:11 15:51:11")
        assert month == "June"

    def test_correct_year(self):
        year = self.PictureActions.getYear("2020:06:11 15:51:11")
        assert year == "2020"

    def test_rename_correct(self):
        new_name = self.PictureActions.newName("2020:06:11 15:51:11", "test.jpg")
        assert new_name == "2020:06:11T15:51:11.jpg"

    def test_new_directory(self):
        new_directory = self.PictureActions.newDir("2020", "June")
        assert new_directory == "../static/photos/img/Photos/2020/June"

    def test_move(self):
        self.PictureActions.move("../static/photos/img/Photos/2020/June", "test.jpg", "2020:06:11T15:51:11.jpg")
        in_temp = os.path.exists('../static/photos/img/tmp/test.jpg')
        in_destination = os.path.exists("../static/photos/img/Photos/2020/June/2020:06:11T15:51:11.jpg")
        assert in_temp == False
        assert in_destination == True
"""

class WholeFlow(unittest.TestCase):
    def test_whole_flow(self):
        upload.PictureActions("test.jpg").completeUpload()
        in_temp = os.path.exists('static/photos/img/tmp/test.jpg')
        in_destination = os.path.exists("static/photos/img/Photos/2020/June/2020:06:11T15:51:11.jpg")
        assert in_temp == False
        assert in_destination == True

    def test_dup_handling(self):
        upload.PictureActions("test_whole.jpg").completeUpload()
        upload.PictureActions("test2.jpg").completeUpload()
        in_temp = os.path.exists('static/photos/img/tmp/test_whole.jpg')
        initial_in_destination = os.path.exists("static/photos/img/Photos/2020/June/2020:06:11T15:51:11.jpg")
        second_in_destination = os.path.exists("static/photos/img/Photos/2020/June/2020:06:11T15:51:11_1.jpg")
        assert in_temp == False
        assert initial_in_destination == True
        assert second_in_destination == True


if __name__ == '__main__':
    unittest.main(verbosity=1)