import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Photos import viewPhotos

class File_Location(unittest.TestCase):

    def setUp(self):
        self.ViewPhotos = viewPhotos.ViewPhotos()
    
    def test_get_location(self):
        """First Location should be Photos/"""
        location = self.ViewPhotos.location
        assert location == "Photos/"

    def test_files_in_location(self):
        """Files in top location should be 2020"""
        contents = self.ViewPhotos.contents
        assert contents['directory']['contents'][0]["name"] == "2020"

    def test_file_is_directory(self):
        """Contents of top location should be 2020 - Directory: True"""
        contents = self.ViewPhotos.contents
        assert contents['directory']['contents'][0]["is_directory"] == True



if __name__ == '__main__':
    unittest.main(verbosity=1)