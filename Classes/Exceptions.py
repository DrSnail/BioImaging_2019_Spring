class ImageError(Exception):
    def __str__(self):
        return "Error"

class ImageIsNotPresented(ImageError):
    def __str__(self):
        return "Image has to be specifed before using"

class GrayImageError(ImageError):
    def __str__(self):
        return "Gray Image Error"

class GrayIncorrectCreatingError(GrayImageError):
    def __str__(self):
        return "Class Gray has to be created via method _convert_to_gray of class Image"