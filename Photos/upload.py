from werkzeug.utils import secure_filename
from exif import Image
import os
import shutil
import glob
from PIL import Image as PIL_Image
from PIL.ExifTags import TAGS

class Upload:
    def __init__(self, file):
        self.file = file

    def tempStore(self):
        if self.file.filename == '':
            return False
        elif self.file and self.allowed_file(self.file.filename):
            upload_folder = 'static/photos/img/tmp'
            filename = secure_filename(self.file.filename)
            print(os.path.join(upload_folder, filename))
            self.file.save(os.path.join(upload_folder, filename))
            return True
        else:
            return False


    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class PictureActions:
    def __init__(self, imageList):
        self.imageList = imageList
        #self.processImages()
        #self.setUpImg()
        #datetime = self.getDT()

    def processImages(self):
        for file in self.imageList:
            print(file)
            self.filename = file
            self.setUpImg()
            self.create_thumbnail()
            self.completeUpload()
        return True

        #for infile in glob.glob("./static/photos/img/tmp/*.*"):
        #    file, ext = os.path.splitext(infile)
        #    print(file)
        #   print(ext)
        #    self.checkOrienation()
        #    im = PIL_Image.open(infile)
        #    im.thumbnail(size, PIL_Image.ANTIALIAS)
        #    im.save(file + (".thumbnail{}").format(ext))

    def setUpImg(self):
        upload_folder = 'static/photos/img/tmp'
        with open(os.path.join(upload_folder, self.filename), 'rb') as image_file:
                self.my_image = Image(image_file)
        i = PIL_Image.open(os.path.join(upload_folder, self.filename))
        info = i._getexif()
        self.image_orientation = ({TAGS.get(tag): value for tag, value in info.items()})['Orientation']

    def create_thumbnail(self):
        size = 128, 128
        upload_folder = 'static/photos/img/tmp'
        file = self.filename.split(".")[0]
        ext = ".{}".format(self.filename.split(".")[1])
        im = PIL_Image.open(os.path.join(upload_folder, self.filename))
        im.thumbnail(size, PIL_Image.ANTIALIAS)
        im = self.checkRotation(im)
        im.save(("{}/{}.thumbnail{}").format(upload_folder, file, ext))

    def checkRotation(self, image):
        print(self.image_orientation)
        if self.image_orientation == 3:
            image=image.rotate(180, expand=True)
        elif self.image_orientation == 6:
            image=image.rotate(270, expand=True)
        elif self.image_orientation == 8:
            image=image.rotate(90, expand=True)
        return image



    def completeUpload(self):
        datetime = self.getDT()
        month = self.getMonth(datetime)
        year = self.getYear(datetime)
        new_name = self.newName(datetime, self.filename)
        new_dir = self.newDir(year, month)
        self.move(new_dir, self.filename, new_name)
        self.move_thumbnail(new_dir, new_name)

    def move_thumbnail(self, new_dir, new_name):
        split_name = self.filename.split(".")
        thumbnail = "{}.thumbnail.{}".format(split_name[0], split_name[1])
        split_new_name = new_name.split(".")
        thumbnail_new = "{}.thumbnail.{}".format(split_new_name[0], split_new_name[1])
        self.move(new_dir, thumbnail, thumbnail_new)

    def getDT(self):
        return self.my_image.datetime_original

    def getMonth(self, datetime):
        months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = int(datetime.split(":")[1])
        print(months[month])
        return months[month]

    def getYear(self, datetime):
        return datetime.split(":")[0]

    def newName(self, datetime, filename):
        datetime = datetime.split(" ")
        return "{}T{}.{}".format(datetime[0], datetime[1], filename.split(".")[1])

    def newDir(self, year, month):
        new_dir = "static/photos/img/Photos/{}/{}".format(year, month)
        self.checkPath(new_dir)
        return new_dir

    def checkPath(self, new_dir):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

    def move(self, new_dir, filename, new_name):
        current_path = "static/photos/img/tmp/{}".format(filename)
        new_path = "{}/{}".format(new_dir, new_name)
        new_path = self.checkExists(new_path, new_name, new_dir, new_name)
        print(current_path)
        print(new_path)
        shutil.move(current_path, new_path)

    def checkExists(self, new_path, new_name, new_dir, filename):
        current_path = new_path
        unique = False
        number_attempt = 0
        while not unique:
            file_exists = os.path.exists(current_path)
            if file_exists:
                file_split = filename.split(".")
                number_attempt+=1
                if new_path == current_path:
                    current_path = "{}/{}_{}.{}".format(new_dir, file_split[0], number_attempt, file_split[1])
                else:
                    current_path = "{}/{}_{}.{}".format(new_dir, file_split[0], number_attempt, file_split[1])
            else:
                unique = True
        return current_path
            


