import os
from io import BytesIO
from PIL import Image as Img
from django.core.files.uploadedfile import InMemoryUploadedFile


class ImageQualityHandler:
    inputFile = None
    longest_side = None
    image_quality = None

    def __init__(self, inputFile, longest_side, image_quality):
        self.inputFile = inputFile
        self.longest_side = longest_side
        self.image_quality = image_quality

    def get_InMemoryUploadedFile(self):
        img = Img.open(BytesIO(self.inputFile.read()))
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize(self.get_dimension(img, self.longest_side), Img.ANTIALIAS)
        output = BytesIO()
        img.rotate(-90).save(output, format='JPEG', quality=self.image_quality)
        output.seek(0)
        return InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.inputFile.name.split('.')[0], 'image/jpeg', output.seek(0, 2), None)


    def get_dimension(self, img, longest_side):
        size = [img.width, img.height]
        pointer_big = 0
        pointer_small = 1

        if img.width <= img.height:
            pointer_big = 1
            pointer_small = 0


        size[pointer_small] = (size[pointer_small] / size[pointer_big]) * longest_side
        size[pointer_big] = longest_side

        return (int(size[0]), int(size[1]))
