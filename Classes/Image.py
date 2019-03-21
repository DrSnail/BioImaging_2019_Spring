import cv2

class Image:
    def __init__(self, address: str):
        self._address = address
        pass

class Grey_Image(Image):
    def __init__(self, address: str):
        super().__init__(address)
        pass

class Edged_Image(Image):
    def __init__(self, address: str):
        super(Edged_Image, self).__init__(address)
        pass

class Closed_Image(Image):
    def __init__(self, address: str):
        super(Closed_Image, self).__init__(address)
        pass