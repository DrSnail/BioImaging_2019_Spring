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

class EdgeImageError(ImageError):
    def __str__(self):
        return "Edge Image Error"

class EdgeIncorrectCreatingError(EdgeImageError):
    def __str__(self):
        return "Class Edge has to be created via method _edge_finding of class Gray"

class ClosedImageError(ImageError):
    def __str__(self):
        return "Closed Image Error"

class ClosedIncorrectCreatingError(ClosedImageError):
    def __str__(self):
        return "Class Closed has to be created via method _get_closed_class of class Edge"