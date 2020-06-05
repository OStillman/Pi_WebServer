import os

"""
{
  "directory": {
    "contents": [
      {
        "name": "Test",
        "is_directory": false
      }
      ]
  }
}
"""

class ViewPhotos():
    def __init__(self, location=None, contents=None):
        self.begin()
        self.getContents()
        self.sortContents()

    def begin(self):
        self.location = "Photos/"

    def getContents(self):
        location = "/home/pi/{}".format(self.location)
        these_files = os.listdir(location)
        print(these_files)
        self.contents = these_files

    def sortContents(self):
        end_data = {"directory": {"contents": []}}
        for file in self.contents:
            is_directory = True
            if "." in file:
                is_directory = False
            end_data['directory']['contents'].append({"name": file, "is_directory": is_directory})
        #print(end_data)
        self.contents = end_data


    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, contents):
        self._contents = contents