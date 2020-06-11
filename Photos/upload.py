from werkzeug.utils import secure_filename
from exif import Image
import os

class Upload:
    def __init__(self, file):
        self.file = file

    def tempStore(self):
        if self.file.filename == '':
            return False
        elif self.file and self.allowed_file(self.file.filename):
            upload_folder = 'static/photos/img/Photos'
            filename = secure_filename(self.file.filename)
            print(os.path.join(upload_folder, filename))
            self.file.save(os.path.join(upload_folder, filename))
            with open(os.path.join(upload_folder, filename), 'rb') as image_file:
                my_image = Image(image_file)
            print(dir(my_image))
            print(my_image.get_thumbnail)
            return True
        else:
            return False


    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS