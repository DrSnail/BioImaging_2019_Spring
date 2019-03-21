class ImageError(Exception):
    def __str__(self):
        return "Error"

class ImageIsNotPresented(ImageError):
    def __str__(self):
        return "Image have to be specifed before using"

class GrayImage(ImageError):
    def __str__(self):
        return "Gray Image Error"