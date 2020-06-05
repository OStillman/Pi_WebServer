import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Photos import viewContents

class File_Location(unittest.TestCase):

    def setUp(self):
        self.ViewContents = viewContents.ViewContents()
    
    def test_get_location(self):
        """First Location should be Photos/"""
        location = self.ViewContents.location
        assert location == "Photos/"

    def test_files_in_location(self):
        """Files in top location should be 2020"""
        contents = self.ViewContents.contents
        assert contents['directory']['contents'][0]["name"] == "2020"

    def test_file_is_directory(self):
        """Contents of top location should be 2020 - Directory: True"""
        contents = self.ViewContents.contents
        assert contents['directory']['contents'][0]["is_directory"] == True


class Traversing_Contents(unittest.TestCase):

    def setUp(self):
        self.ViewContents = viewContents.ViewContents('Photos/2020/')

    def test_parent_directory(self):
        """Parent directory should be 2020"""
        contents = self.ViewContents.contents
        assert "Photos" in contents['directory']['contents'][0]["name"]
        assert contents['directory']['contents'][0]["is_parent"] == True

    def test_files_in_location(self):
        """Moved down one, now should = May"""
        contents = self.ViewContents.contents
        assert contents['directory']['contents'][1]["name"] == "May"
        assert contents['directory']['contents'][1]["is_parent"] == False
    
    def test_traverse_image(self):
        """Should not be able to traverse an image"""
        ViewContents = viewContents.ViewContents('Photos/2020/May/food.jpg')
        assert ViewContents.contents == None


    


if __name__ == '__main__':
    unittest.main(verbosity=1)