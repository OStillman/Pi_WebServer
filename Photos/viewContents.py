import os

"""
{
  "directory": {
    "contents": [
      {
        "name": "Test",
        "is_directory": false,
        "is_parent": false
      }
      ]
  }
}
"""

class ViewContents():
    def __init__(self, directory=None, location=None, contents=None):
        self.directory = directory
        self.begin()
        self.getParent()
        self.getContents()
        self.sortContents()

    def begin(self):
        if not self.directory:
            self.location = "Photos/"
        else:
            self.location = self.directory

    def getParent(self):
        directories = self.location.split("/")
        end_dir_number = len(directories) - 3
        self.parent = directories[end_dir_number]

    def getContents(self):
        location = "/home/pi/{}".format(self.location)
        try:
            these_files = os.listdir(location)
            self.contents = these_files
        except NotADirectoryError:
            self.contents = []
        

    def sortContents(self):
        end_data = {"directory": {"contents": []}}
        if len(self.contents) > 0:
            if len(self.parent) > 0:
                    end_data['directory']['contents'].append({"name": self.parent, "is_directory": True, "is_parent": True, "is_thumbnail": False})
            for file in self.contents:
                is_directory = True
                is_thumbnail = False
                if "." in file:
                    is_directory = False
                    if ".thumbnail" in file:
                        is_thumbnail = True
                end_data['directory']['contents'].append({"name": file, "is_directory": is_directory, "is_parent": False, "is_thumbnail": is_thumbnail})
            #print(end_data)
            self.contents = end_data
        else:
            self.contents = None


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